from datetime import datetime, timezone
from app.schemas.models import (
    ClientRead,
    ClientContextRead,
    KeywordIdeaRead,
    KeywordClusterRead,
    KeywordClusterKeywordRead,
    KeywordSetRead,
    BestAlternateRead,
    BlogIdeaRead,
    BlogPostArtifactRead,
)
from app.utils import get_current_timestamp

# Base timestamp for all demo data
_base_time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)


def get_clients() -> list[ClientRead]:
    """Get hardcoded list of clients."""
    return [
        ClientRead(
            id=1,
            name="Setsail",
            slug="setsail",
            notes="Demo client for Setsail",
            created_at=_base_time,
            updated_at=_base_time,
        ),
        ClientRead(
            id=2,
            name="CleanDesign",
            slug="cleandesign",
            notes="Demo client for CleanDesign",
            created_at=_base_time,
            updated_at=_base_time,
        ),
    ]


def get_client_context(client_id: int) -> ClientContextRead | None:
    """Get hardcoded client context."""
    if client_id == 1:
        return ClientContextRead(
            id=1,
            client_id=1,
            domain="setsail.com",
            call_to_action="Get started with Setsail today",
            about="Setsail is a modern platform for managing your business operations.",
            competitors=["Competitor A", "Competitor B"],
            brand_pov="Innovative and forward-thinking",
            ideal_target_market="Small to medium businesses",
            brand_safety={"level": "high"},
            author_tone="Professional and friendly",
            author_rules=["Be concise", "Use active voice"],
            logos=[],
            colors=["#0066CC", "#FFFFFF"],
            fonts=["Inter", "Arial"],
            images_used=[],
            social_links={"twitter": "https://twitter.com/setsail"},
            company_details={"founded": "2020"},
            questionnaire=[],
            existing_blog_titles=["Getting Started with Setsail"],
            ready=True,
            created_at=_base_time,
            updated_at=_base_time,
        )
    elif client_id == 2:
        return ClientContextRead(
            id=2,
            client_id=2,
            domain="cleandesign.com",
            call_to_action="Transform your design workflow",
            about="CleanDesign provides elegant design solutions for modern businesses.",
            competitors=["Design Co", "Style Inc"],
            brand_pov="Minimalist and elegant",
            ideal_target_market="Design agencies and creative professionals",
            brand_safety={"level": "medium"},
            author_tone="Creative and inspiring",
            author_rules=["Show, don't tell", "Use visual language"],
            logos=[],
            colors=["#000000", "#FFFFFF", "#FF6B6B"],
            fonts=["Helvetica", "Georgia"],
            images_used=[],
            social_links={"instagram": "https://instagram.com/cleandesign"},
            company_details={"founded": "2018"},
            questionnaire=[],
            existing_blog_titles=["Design Trends 2024"],
            ready=True,
            created_at=_base_time,
            updated_at=_base_time,
        )
    return None


def get_keyword_ideas(client_id: int) -> list[KeywordIdeaRead]:
    """Get hardcoded keyword ideas."""
    if client_id == 1:
        return [
            KeywordIdeaRead(
                id=1,
                client_id=1,
                keyword="business management software",
                source="demo",
                search_volume=1200,
                keyword_difficulty=45,
                created_at=_base_time,
            ),
            KeywordIdeaRead(
                id=2,
                client_id=1,
                keyword="project management tools",
                source="demo",
                search_volume=2400,
                keyword_difficulty=55,
                created_at=_base_time,
            ),
        ]
    elif client_id == 2:
        return [
            KeywordIdeaRead(
                id=3,
                client_id=2,
                keyword="web design services",
                source="demo",
                search_volume=1800,
                keyword_difficulty=50,
                created_at=_base_time,
            ),
            KeywordIdeaRead(
                id=4,
                client_id=2,
                keyword="UI design trends",
                source="demo",
                search_volume=900,
                keyword_difficulty=40,
                created_at=_base_time,
            ),
        ]
    return []


def get_keyword_clusters(client_id: int) -> list[KeywordClusterRead]:
    """Get hardcoded keyword clusters."""
    if client_id == 1:
        return [
            KeywordClusterRead(
                id=1,
                client_id=1,
                label="Business Management",
                created_at=_base_time,
                updated_at=_base_time,
                keywords=[
                    KeywordClusterKeywordRead(
                        id=1,
                        cluster_id=1,
                        keyword="business management",
                        search_volume=1200,
                        keyword_difficulty=45,
                        intent=2,
                        quality=0.85,
                        created_at=_base_time,
                        updated_at=_base_time,
                    ),
                ],
            ),
        ]
    elif client_id == 2:
        return [
            KeywordClusterRead(
                id=2,
                client_id=2,
                label="Design Services",
                created_at=_base_time,
                updated_at=_base_time,
                keywords=[
                    KeywordClusterKeywordRead(
                        id=2,
                        cluster_id=2,
                        keyword="web design",
                        search_volume=1800,
                        keyword_difficulty=50,
                        intent=3,
                        quality=0.90,
                        created_at=_base_time,
                        updated_at=_base_time,
                    ),
                ],
            ),
        ]
    return []


def get_keyword_sets(client_id: int) -> list[KeywordSetRead]:
    """Get hardcoded keyword sets."""
    if client_id == 1:
        return [
            KeywordSetRead(
                id=1,
                client_id=1,
                primary_keyword="business management software",
                primary_search_volume=1200,
                primary_keyword_difficulty=45,
                primary_intent=2,
                primary_quality=0.85,
                secondaries=[
                    {"keyword": "project management", "sv": 2400, "kd": 55},
                    {"keyword": "team collaboration", "sv": 1800, "kd": 50},
                ],
                created_at=_base_time,
                updated_at=_base_time,
            ),
        ]
    elif client_id == 2:
        return [
            KeywordSetRead(
                id=2,
                client_id=2,
                primary_keyword="web design services",
                primary_search_volume=1800,
                primary_keyword_difficulty=50,
                primary_intent=3,
                primary_quality=0.90,
                secondaries=[
                    {"keyword": "UI design", "sv": 1200, "kd": 45},
                    {"keyword": "responsive design", "sv": 900, "kd": 40},
                ],
                created_at=_base_time,
                updated_at=_base_time,
            ),
        ]
    return []


def get_best_alternates(client_id: int) -> list[BestAlternateRead]:
    """Get hardcoded best alternates."""
    if client_id == 1:
        return [
            BestAlternateRead(
                id=1,
                client_id=1,
                original_keyword_id=1,
                keyword="business management software",
                search_volume=1200,
                keyword_difficulty=45,
                is_original=True,
                created_at=_base_time,
                updated_at=_base_time,
            ),
        ]
    elif client_id == 2:
        return [
            BestAlternateRead(
                id=2,
                client_id=2,
                original_keyword_id=3,
                keyword="web design services",
                search_volume=1800,
                keyword_difficulty=50,
                is_original=True,
                created_at=_base_time,
                updated_at=_base_time,
            ),
        ]
    return []


def get_blog_ideas(client_id: int) -> list[BlogIdeaRead]:
    """Get hardcoded blog ideas."""
    if client_id == 1:
        return [
            BlogIdeaRead(
                id=1,
                client_id=1,
                topic="How to Choose the Right Business Management Software",
                keyword_set_id=1,
                state="complete",
                error_message=None,
                brief_json={"target_length": 2000},
                latest_sq_report={"score": 85},
                iteration_count=1,
                draft_html=None,
                created_at=_base_time,
                updated_at=_base_time,
            ),
        ]
    elif client_id == 2:
        return [
            BlogIdeaRead(
                id=2,
                client_id=2,
                topic="Top Web Design Trends for 2024",
                keyword_set_id=2,
                state="complete",
                error_message=None,
                brief_json={"target_length": 1800},
                latest_sq_report={"score": 90},
                iteration_count=1,
                draft_html=None,
                created_at=_base_time,
                updated_at=_base_time,
            ),
        ]
    return []


def get_blog_post_artifact(blog_post_id: int) -> BlogPostArtifactRead | None:
    """Get hardcoded blog post artifact."""
    if blog_post_id == 1:
        return BlogPostArtifactRead(
            id=1,
            client_id=1,
            blog_idea_id=1,
            title="How to Choose the Right Business Management Software",
            slug="how-to-choose-business-management-software",
            html_body="<h1>How to Choose the Right Business Management Software</h1><p>Demo content...</p>",
            markdown_body="# How to Choose the Right Business Management Software\n\nDemo content...",
            meta_title="How to Choose Business Management Software | Setsail",
            meta_description="Learn how to choose the right business management software for your needs.",
            meta_keywords=["business management", "software", "tools"],
            xml=None,
            raw_response={},
            schema_json_ld={},
            images=[],
            seo_score=85.0,
            summary="A comprehensive guide to choosing business management software.",
            title_tag="How to Choose the Right Business Management Software",
            created_at=_base_time,
            updated_at=_base_time,
        )
    elif blog_post_id == 2:
        return BlogPostArtifactRead(
            id=2,
            client_id=2,
            blog_idea_id=2,
            title="Top Web Design Trends for 2024",
            slug="top-web-design-trends-2024",
            html_body="<h1>Top Web Design Trends for 2024</h1><p>Demo content...</p>",
            markdown_body="# Top Web Design Trends for 2024\n\nDemo content...",
            meta_title="Top Web Design Trends for 2024 | CleanDesign",
            meta_description="Discover the latest web design trends shaping 2024.",
            meta_keywords=["web design", "trends", "2024"],
            xml=None,
            raw_response={},
            schema_json_ld={},
            images=[],
            seo_score=90.0,
            summary="An overview of the top web design trends for 2024.",
            title_tag="Top Web Design Trends for 2024",
            created_at=_base_time,
            updated_at=_base_time,
        )
    return None


def get_blog_idea_html(blog_idea_id: int, version_number: int | None = None) -> dict | None:
    """Get hardcoded HTML for a blog idea."""
    version = version_number if version_number is not None else 1
    if blog_idea_id == 1:
        return {
            "blog_idea_id": 1,
            "version_number": version,
            "html": "<h1>How to Choose the Right Business Management Software</h1><p>Demo HTML content...</p>",
        }
    elif blog_idea_id == 2:
        return {
            "blog_idea_id": 2,
            "version_number": version,
            "html": "<h1>Top Web Design Trends for 2024</h1><p>Demo HTML content...</p>",
        }
    return None

