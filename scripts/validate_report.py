#!/usr/bin/env python3
"""
Report Validation Script
Ensures modular research reports meet quality standards before delivery.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List

class ReportValidator:
    """Validates modular research report quality"""

    def __init__(self, report_dir: Path):
        self.report_dir = Path(report_dir)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
        # Will store all file contents to check across the whole report
        self.all_content = ""
        self.files_found = []

    def validate(self) -> bool:
        """Run all validation checks"""
        print(f"\n{'='*60}")
        print(f"VALIDATING MODULAR REPORT: {self.report_dir.name}")
        print(f"{'='*60}\n")

        if not self.report_dir.is_dir():
            print(f"❌ ERROR: {self.report_dir} is not a directory.")
            print("Usage: python validate_report.py --report path/to/report_directory")
            sys.exit(1)

        self._load_files()

        checks = [
            ("Required Files", self._check_required_files),
            ("Executive Summary", self._check_executive_summary),
            ("Findings Directory", self._check_findings),
            ("Global Citations", self._check_citations),
            ("Bibliography", self._check_bibliography),
            ("Placeholder Text", self._check_placeholders),
            ("Content Truncation", self._check_content_truncation),
        ]

        for check_name, check_func in checks:
            print(f"⏳ Checking: {check_name}...", end=" ")
            passed = check_func()
            if passed:
                print("✅ PASS")
            else:
                print("❌ FAIL")

        self._print_summary()

        return len(self.errors) == 0

    def _load_files(self):
        """Load all markdown files into memory for cross-checking"""
        for md_file in self.report_dir.rglob("*.md"):
            try:
                content = md_file.read_text(encoding='utf-8')
                self.all_content += f"\n\n--- FILE: {md_file.name} ---\n\n{content}"
                self.files_found.append(md_file.relative_to(self.report_dir))
            except Exception as e:
                self.errors.append(f"Failed to read {md_file}: {e}")

    def _check_required_files(self) -> bool:
        """Check all required files are present"""
        required = [
            Path("summary.md"),
            Path("synthesis.md"),
            Path("limitations.md"),
            Path("recommendations.md"),
            Path("bibliography.md")
        ]

        missing = []
        for req in required:
            if req not in self.files_found:
                missing.append(str(req))

        if missing:
            self.errors.append(f"Missing required files: {', '.join(missing)}")
            return False
            
        return True

    def _check_executive_summary(self) -> bool:
        """Check summary.md is under 400 words"""
        summary_path = self.report_dir / "summary.md"
        if not summary_path.exists():
            return False

        content = summary_path.read_text(encoding='utf-8')
        word_count = len(content.split())

        if word_count > 400:
            self.warnings.append(f"summary.md too long: {word_count} words (should be ≤400)")
        if word_count < 50:
            self.warnings.append(f"summary.md too short: {word_count} words (should be ≥50)")

        return True

    def _check_findings(self) -> bool:
        """Check findings directory exists and has files"""
        findings_dir = self.report_dir / "findings"
        if not findings_dir.is_dir():
            self.errors.append("Missing 'findings' directory")
            return False
            
        findings_files = list(findings_dir.glob("*.md"))
        if not findings_files:
            self.errors.append("No finding files found in 'findings/' directory")
            return False
            
        return True

    def _check_citations(self) -> bool:
        """Check citation format in all files"""
        # Find all citation references [1], [2], etc.
        citations = re.findall(r'\[(\d+)\]', self.all_content)

        if not citations:
            self.errors.append("No citations [N] found in any report files")
            return False

        unique_citations = set(citations)

        if len(unique_citations) < 10:
            self.warnings.append(f"Only {len(unique_citations)} unique sources cited globally (recommended: ≥10)")

        return True

    def _check_bibliography(self) -> bool:
        """Check bibliography format and completeness"""
        bib_path = self.report_dir / "bibliography.md"
        if not bib_path.exists():
            return False

        bib_content = bib_path.read_text(encoding='utf-8')

        # Find bibliography entries
        bib_entries = re.findall(r'^\[(\d+)\]', bib_content, re.MULTILINE)

        if not bib_entries:
            self.errors.append("Bibliography.md has no valid entries starting with [N]")
            return False

        # Find all citations used in OTHER files
        other_content = self.all_content.replace(bib_content, "")
        text_citations = set(re.findall(r'\[(\d+)\]', other_content))
        bib_citations = set(bib_entries)

        # Check all citations have bibliography entries
        missing_in_bib = text_citations - bib_citations
        if missing_in_bib:
            self.errors.append(f"Citations used in text but missing from bibliography.md: {sorted(missing_in_bib, key=int)}")
            return False

        return True

    def _check_placeholders(self) -> bool:
        """Check for placeholder text"""
        placeholders = [
            'TBD', 'TODO', 'FIXME', 'XXX',
            '[citation needed]', '[needs citation]',
            '[placeholder]', '[TODO]', '[TBD]'
        ]

        found_placeholders = []
        for placeholder in placeholders:
            if placeholder in self.all_content:
                found_placeholders.append(placeholder)

        if found_placeholders:
            self.errors.append(f"Found placeholder text somewhere in report: {', '.join(found_placeholders)}")
            return False

        return True

    def _check_content_truncation(self) -> bool:
        """Check for content truncation patterns"""
        truncation_patterns = [
            (r'Content continues', 'Phrase "Content continues"'),
            (r'Due to length', 'Phrase "Due to length"'),
            (r'would continue', 'Phrase "would continue"'),
            (r'Additional sections', 'Phrase "Additional sections"'),
        ]

        for pattern_re, description in truncation_patterns:
            if re.search(pattern_re, self.all_content, re.IGNORECASE):
                self.errors.append(f"⚠️ CRITICAL: Content truncation detected: {description}")
                return False

        return True

    def _print_summary(self):
        """Print validation summary"""
        print(f"\n{'='*60}")
        print("VALIDATION SUMMARY")
        print(f"{'='*60}")

        if self.errors:
            print(f"\n❌ FAILED ({len(self.errors)} errors):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")
        else:
            print("\n✅ PASSED (0 errors)")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        print("\n")


def main():
    parser = argparse.ArgumentParser(description="Validate modular research report quality")
    parser.add_argument("--report", required=True, help="Path to the report directory")
    args = parser.parse_args()

    # Backwards compatibility: if they point to summary.md, use its parent dir
    report_path = Path(args.report)
    if report_path.is_file() and report_path.name == 'summary.md':
        report_path = report_path.parent

    validator = ReportValidator(report_path)
    is_valid = validator.validate()

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
