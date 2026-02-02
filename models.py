import uuid
from sqlalchemy import Column, String, Boolean, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base

# ---------------- ORGANIZATION ----------------
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    plan_type = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


# ---------------- USER ----------------
class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255))
    full_name = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    last_login = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


# ---------------- REPOSITORY ----------------
class Repository(Base):
    __tablename__ = "repositories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    provider = Column(String(50), nullable=False)
    repo_name = Column(String(255), nullable=False)
    repo_url = Column(String(500), nullable=False)
    default_branch = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    connected_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


# ---------------- DOCUMENTATION RUN ----------------
class DocumentationRun(Base):
    __tablename__ = "documentation_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    repository_id = Column(UUID(as_uuid=True), ForeignKey("repositories.id"))
    triggered_by = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    files_scanned = Column(Integer)
    output_path = Column(String(500))
    started_at = Column(TIMESTAMP(timezone=True))
    completed_at = Column(TIMESTAMP(timezone=True))


# ---------------- PULL REQUEST ----------------
class PullRequest(Base):
    __tablename__ = "pull_requests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    repository_id = Column(UUID(as_uuid=True), ForeignKey("repositories.id"))
    pr_number = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


# ---------------- CODE REVIEW RUN ----------------
class CodeReviewRun(Base):
    __tablename__ = "code_review_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pull_request_id = Column(UUID(as_uuid=True), ForeignKey("pull_requests.id"))
    triggered_by = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    files_analyzed = Column(Integer)
    started_at = Column(TIMESTAMP(timezone=True))
    completed_at = Column(TIMESTAMP(timezone=True))


# ---------------- REVIEW FINDING ----------------
class ReviewFinding(Base):
    __tablename__ = "review_findings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    review_run_id = Column(UUID(as_uuid=True), ForeignKey("code_review_runs.id"))
    file_path = Column(String(500), nullable=False)
    line_number = Column(Integer)
    issue_type = Column(String(50), nullable=False)
    severity = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    suggestion = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
