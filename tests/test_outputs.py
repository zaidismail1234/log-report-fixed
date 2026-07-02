from pathlib import Path


def test_report_exists():
    """report.json must exist"""
    assert Path("/app/report.json").exists()


def test_report_nonempty():
    """report.json must not be empty"""
    assert Path("/app/report.json").stat().st_size > 0