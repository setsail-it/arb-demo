from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict


# Client Schemas
class ClientBase(BaseModel):
    name: str
    slug: str | None = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    notes: str | None = None


class ClientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str | None
    notes: str | None
    created_at: datetime
    updated_at: datetime


# ClientContext Schemas
class ClientContextBase(BaseModel):
    domain: str
    call_to_action: str | None = None
    about: str | None = None
    competitors: list[str] | None = None
    brand_pov: str | None = None
    ideal_target_market: str | None = None
    brand_safety: dict | None = None
    author_tone: str | None = None
    author_rules: list[str] | None = None
    logos: list[Any] | None = None
    colors: list[str] | None = None
    fonts: list[str] | None = None
    images_used: list[str] | None = None
    social_links: dict[str, str | None] | None = None
    company_details: dict[str, Any] | None = None
    questionnaire: list[dict[str, str]] | None = None
    existing_blog_titles: list[str] | None = None
    ready: bool | None = None


class ClientContextCreate(ClientContextBase):
    pass


class ClientContextUpdate(BaseModel):
    domain: str | None = None
    call_to_action: str | None = None
    about: str | None = None
    competitors: list[str] | None = None
    brand_pov: str | None = None
    ideal_target_market: str | None = None
    brand_safety: dict | None = None
    author_tone: str | None = None
    author_rules: list[str] | None = None
    logos: list[Any] | None = None
    colors: list[str] | None = None
    fonts: list[str] | None = None
    images_used: list[str] | None = None
    social_links: dict[str, str | None] | None = None
    company_details: dict[str, Any] | None = None
    questionnaire: list[dict[str, str]] | None = None
    existing_blog_titles: list[str] | None = None
    ready: bool | None = None


class ClientContextRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    domain: str
    call_to_action: str | None
    about: str | None
    competitors: list[str] | None
    brand_pov: str | None
    ideal_target_market: str | None
    brand_safety: dict | None
    author_tone: str | None
    author_rules: list[str] | None
    logos: list[Any] | None
    colors: list[str] | None
    fonts: list[str] | None
    images_used: list[str] | None
    social_links: dict[str, str | None] | None
    company_details: dict[str, Any] | None
    questionnaire: list[dict[str, str]] | None
    existing_blog_titles: list[str] | None
    ready: bool
    created_at: datetime
    updated_at: datetime


# KeywordIdea Schemas
class KeywordIdeaBase(BaseModel):
    keyword: str
    source: str | None = None


class KeywordIdeaCreate(KeywordIdeaBase):
    pass


class KeywordIdeaUpdate(BaseModel):
    keyword: str | None = None
    source: str | None = None


class KeywordIdeaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    keyword: str
    source: str | None
    search_volume: int | None = None
    keyword_difficulty: int | None = None
    created_at: datetime


# KeywordClusterKeyword Schemas
class KeywordClusterKeywordBase(BaseModel):
    keyword: str
    search_volume: int | None = None
    keyword_difficulty: int | None = None
    intent: int | None = None
    quality: float | None = None


class KeywordClusterKeywordCreate(KeywordClusterKeywordBase):
    pass


class KeywordClusterKeywordUpdate(BaseModel):
    keyword: str | None = None
    search_volume: int | None = None
    keyword_difficulty: int | None = None
    intent: int | None = None
    quality: float | None = None


class KeywordClusterKeywordRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cluster_id: int
    keyword: str
    search_volume: int | None
    keyword_difficulty: int | None
    intent: int | None
    quality: float | None
    created_at: datetime
    updated_at: datetime


# KeywordCluster Schemas
class KeywordClusterBase(BaseModel):
    label: str


class KeywordClusterCreate(KeywordClusterBase):
    pass


class KeywordClusterUpdate(BaseModel):
    label: str | None = None


class KeywordClusterRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    label: str
    created_at: datetime
    updated_at: datetime
    keywords: list[KeywordClusterKeywordRead] | None = None


# KeywordSet Schemas
class KeywordSetBase(BaseModel):
    primary_keyword: str
    primary_search_volume: int | None = None
    primary_keyword_difficulty: int | None = None
    primary_intent: int | None = None
    primary_quality: float | None = None
    secondaries: list[dict] | None = None


class KeywordSetCreate(KeywordSetBase):
    pass


class KeywordSetUpdate(BaseModel):
    primary_keyword: str | None = None
    primary_search_volume: int | None = None
    primary_keyword_difficulty: int | None = None
    primary_intent: int | None = None
    primary_quality: float | None = None
    secondaries: list[dict] | None = None


class KeywordSetRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    primary_keyword: str
    primary_search_volume: int | None
    primary_keyword_difficulty: int | None
    primary_intent: int | None
    primary_quality: float | None
    secondaries: list[dict] | None
    created_at: datetime
    updated_at: datetime


# BestAlternate Schemas
class BestAlternateBase(BaseModel):
    original_keyword_id: int
    keyword: str
    search_volume: int | None = None
    keyword_difficulty: int | None = None
    is_original: bool = False


class BestAlternateCreate(BestAlternateBase):
    pass


class BestAlternateUpdate(BaseModel):
    keyword: str | None = None
    search_volume: int | None = None
    keyword_difficulty: int | None = None
    is_original: bool | None = None


class BestAlternateRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    original_keyword_id: int
    keyword: str
    search_volume: int | None
    keyword_difficulty: int | None
    is_original: bool
    created_at: datetime
    updated_at: datetime


# BlogIdea Schemas
class BlogIdeaBase(BaseModel):
    topic: str
    keyword_set_id: int | None = None
    state: str | None = None
    error_message: str | None = None
    brief_json: dict | None = None
    latest_sq_report: dict | None = None
    iteration_count: int | None = None
    draft_html: str | None = None


class BlogIdeaCreate(BlogIdeaBase):
    pass


class BlogIdeaUpdate(BaseModel):
    topic: str | None = None
    keyword_set_id: int | None = None
    state: str | None = None
    error_message: str | None = None
    brief_json: dict | None = None
    latest_sq_report: dict | None = None
    iteration_count: int | None = None
    draft_html: str | None = None


class BlogIdeaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    topic: str
    keyword_set_id: int | None
    state: str
    error_message: str | None
    brief_json: dict | None
    latest_sq_report: dict | None
    iteration_count: int | None
    draft_html: str | None
    created_at: datetime
    updated_at: datetime


# BlogPostArtifact Schemas
class BlogPostArtifactBase(BaseModel):
    title: str
    slug: str
    html_body: str
    markdown_body: str | None = None
    meta_title: str | None = None
    meta_description: str | None = None
    meta_keywords: list[str] | None = None
    xml: str | None = None
    raw_response: dict | None = None
    schema_json_ld: dict | None = None
    images: list[dict] | None = None
    seo_score: float | None = None
    summary: str | None = None
    title_tag: str | None = None


class BlogPostArtifactCreate(BlogPostArtifactBase):
    pass


class BlogPostArtifactUpdate(BaseModel):
    title: str | None = None
    slug: str | None = None
    html_body: str | None = None
    markdown_body: str | None = None
    meta_title: str | None = None
    meta_description: str | None = None
    meta_keywords: list[str] | None = None
    xml: str | None = None
    raw_response: dict | None = None
    schema_json_ld: dict | None = None
    images: list[dict] | None = None
    seo_score: float | None = None
    summary: str | None = None
    title_tag: str | None = None


class BlogPostArtifactRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    blog_idea_id: int | None
    title: str
    slug: str
    html_body: str
    meta_title: str | None
    meta_description: str | None
    meta_keywords: list[str] | None
    xml: str | None
    schema_json_ld: dict | None
    images: list[dict] | None
    seo_score: float | None
    summary: str | None
    title_tag: str | None
    created_at: datetime
    updated_at: datetime


# HTMLArtifact Schemas
class HTMLArtifactBase(BaseModel):
    client_id: int
    blog_idea_id: int
    version_number: int
    html: str


class HTMLArtifactCreate(HTMLArtifactBase):
    pass


class HTMLArtifactUpdate(BaseModel):
    blog_idea_id: int | None = None
    version_number: int | None = None
    html: str | None = None


class HTMLArtifactRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    blog_idea_id: int
    version_number: int
    html: str
    created_at: datetime
    updated_at: datetime

