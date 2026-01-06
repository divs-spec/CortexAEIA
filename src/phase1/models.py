from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class StepRun:
    """Represents a single step in a GitHub Actions job"""
    name: str
    status: str
    conclusion: Optional[str]
    number: int
    log_content: str = ""
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


@dataclass
class JobRun:
    """Represents a job in a GitHub Actions workflow run"""
    id: int
    name: str
    status: str
    conclusion: Optional[str]
    steps: List[StepRun] = field(default_factory=list)
    html_url: str = ""
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


@dataclass
class WorkflowRun:
    """Represents a complete GitHub Actions workflow run"""
    id: int
    name: str
    status: str
    conclusion: Optional[str]
    html_url: str
    head_branch: str
    head_sha: str
    created_at: str
    updated_at: str
    repository: str
    jobs: List[JobRun] = field(default_factory=list)


@dataclass
class ErrorContext:
    """Extracted error information from logs"""
    error_message: str
    error_type: str  # e.g., "test_failure", "build_error", "lint_error"
    line_number: Optional[int] = None
    file_path: Optional[str] = None
    stack_trace: List[str] = field(default_factory=list)
    surrounding_context: List[str] = field(default_factory=list)


@dataclass
class FailureAnalysis:
    """LLM-generated analysis of workflow failure"""
    workflow_run_id: int
    summary: str
    failed_jobs: List[str]
    failed_steps: List[str]
    error_contexts: List[ErrorContext]
    likely_cause: str
    suggested_actions: List[str]
    confidence: float = 0.0  # 0.0 to 1.0
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
