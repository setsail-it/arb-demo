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
            name="SetSail",
            slug="setsail",
            notes="Demo client for SetSail",
            created_at=_base_time,
            updated_at=_base_time,
        ),
        ClientRead(
            id=7,
            name="CleanDesign.ca",
            slug="cleandesign",
            notes="Demo client for CleanDesign.ca",
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
        # Real Setsail Marketing data from production database
        from datetime import datetime
        return ClientContextRead(
            id=2,
            client_id=2,
            domain="setsail.ca",
            call_to_action="Get Started",
            about="Setsail Marketing is a Vancouver-based full-service digital marketing and performance marketing agency founded in 2015. The firm specializes in ROI-focused lead generation and sales growth for ambitious organizations across Canada and the United States, combining performance marketing (PPC and paid media on Google, Meta, LinkedIn, YouTube, TikTok), SEO, social media management, website design and development (including Webflow and Shopify builds), branding and design, video production, email marketing, and AI/CRM automation under one roof. Operating from its main studio at 200-1737 Boundary Rd in Vancouver, with an additional presence in Beaverton, Oregon, Setsail serves cities, utilities, public-sector organizations, e-bike and e-commerce brands, and growth-stage companies. As a Certified B Corporation and certified partner of Google, Meta, Shopify, Klaviyo, and Ahrefs, the agency emphasizes fixed timelines, fixed deliverables, transparent pricing, and measurable ROI. Its in-house 'Marketing Lab' process is built to test, launch, and optimize campaigns in days rather than weeks, and the agency is consistently rated highly on platforms like Clutch, The Manifest, Capterra, and review sites for creativity, communication, and performance.",
            competitors=[
                "Mediaforce Digital Marketing Agency",
                "Marwick Marketing",
                "Optimized Webmedia",
                "Blue Meta",
                "Vireo Video",
                "Guaranteed SEO",
                "Forge & Spark Media",
                "Longhouse Branding & Marketing",
                "Pound & Grain"
            ],
            brand_pov="We believe modern marketing should be ruthlessly accountable to business outcomes, not vanity metrics. That means every campaign we run must be traceable to leads, revenue, and long-term growth—not just impressions or clicks. Instead of operating as a loose collective of freelancers, we've built a senior, in-house team that controls the entire customer journey: ads, web, video, design, email, and automation working together in a single studio. Our Marketing Lab™ is designed to launch, test, and iterate campaigns in days, giving clients real benchmarks, clear projections, and strategies they can take to the bank. Fixed timelines, fixed deliverables, and fixed pricing are non-negotiables because we want clients to understand exactly what they're getting and when. If we can't show a path to profit, we won't sell the service.\n\nWe also believe performance and principles should coexist. As a Certified B Corporation and partner to platforms like Google, Meta, Shopify, and Klaviyo, we pair enterprise-grade tools with transparent, sustainable business practices. Our stance is that clients deserve a marketing partner who is as invested in their outcomes as they are—one that brings data, creative, and automation together to consistently improve ROAS, lower cost per lead, and compound results over time. We see ourselves as an extension of our clients' teams, focused on long-term partnerships with organizations that value clear communication, cultural fit, and a relentless focus on measurable results.",
            ideal_target_market="Setsail Marketing is best suited for North American organizations with established revenue (typically $1M+ annually) that need predictable, scalable digital acquisition rather than piecemeal tactics. Ideal clients include small to mid-market businesses and mid-level enterprises seeking ROI-driven PPC and performance marketing; e-commerce and direct-to-consumer brands (including e-bike and mobility companies) that require full-funnel campaigns, conversion-focused websites, and ongoing optimization; local and regional service businesses (construction, trades, real estate, professional services, healthcare) looking to turn online traffic into booked jobs; and governments, municipalities, utilities, and impact-driven or B Corp-aligned brands that need a trusted, creative, and accountable partner for campaigns, public awareness, and digital transformation. Decision-makers are typically marketing directors, founders, or leadership teams who value senior talent, strategic thinking, and transparent reporting, and who prefer a single integrated agency that can handle ads, web, creative, and automation end-to-end over the lowest-cost vendor.",
            brand_safety={
                "disallowed_tones": [
                    "Deceptive or misleading (e.g., implying guaranteed outcomes that can't be substantiated).",
                    "Over-hyped, scammy, or \"get rich quick\" style messaging.",
                    "Fear-mongering, shaming, or manipulative emotional pressure.",
                    "Aggressive, hostile, or insulting language toward any group.",
                    "Greenwashing or impact-washing that conflicts with B Corp and ethical positioning."
                ],
                "disallowed_claims": [
                    "Guaranteed revenue or profit claims (e.g., \"We guarantee to double your sales\").",
                    "Unverifiable performance numbers not backed by data or case studies.",
                    "Statements implying insider access, secret hacks, or zero-risk results.",
                    "Claims of being \"the only\" or \"number one\" without credible evidence.",
                    "Any claims that contradict transparent, fixed-fee, ROI-focused positioning (e.g., hidden fees, bait-and-switch offers)."
                ],
                "sensitive_topics": [
                    "Political campaigning or partisan advocacy outside of values-aligned, transparent work.",
                    "Health, medical, or therapeutic claims that could be construed as regulated advice.",
                    "Financial/investment products promising unrealistic returns.",
                    "Adult, gambling, or other high-risk/brand-unsafe industries.",
                    "Misinformation, disinformation, or conspiracy-related content."
                ]
            },
            author_tone="Professional, transparent, data-driven, results-focused, collaborative, confident, no-hype",
            author_rules=[
                "Focus on measurable outcomes (leads, sales, ROAS/ROI), not vanity metrics.",
                "Emphasize fixed timelines, fixed deliverables, and fixed pricing.",
                "Reference data, market research, and clear KPIs.",
                "Highlight speed of execution and cross-functional collaboration.",
                "Avoid hype; use plain, transparent language.",
                "Tie tactics to the customer journey and conversion impact.",
                "Provide clear reporting and actionable insights."
            ],
            logos=[
                "https://cdn.prod.website-files.com/64010eda60ee3b61455c8188/678b6449147ceb057e17ba9a_setsail%20logo%2001.svg"
            ],
            colors=[
                "#00BFA5",
                "#1A1A1A",
                "#F5F5F5"
            ],
            fonts=[
                "Inter",
                "Roboto",
                "Helvetica Neue"
            ],
            images_used=[
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/686dcb71427330e02ed54337_Google%20vs%20Meta%20%E2%80%93%20setsail.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/6883f4314ea4a0f655c7b31a_Hype%20is%20a%20sales%20strategy.%20Not%20an%20investment%20advice%20for%20you.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/6876f506d771022759213fc5_Secrets%20to%20High-Quality%20Leads_%20Proven%20Digital%20Marketing%20Agency%20Strategies.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/687320479c8e614d2e91b5ad_Setsail%20Marketing%20SEO%20Post.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/686a2bf4b02a1cb56f78f381_Podcast%20-%20How%20to%20Know%20If%20Your%20Marketing%20Is%20Actually%20Working.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/6840e040204c708f3270a891_ChatGPT%20Image%20Jun%204%2C%202025%2C%2005_09_20%20PM%20(1).avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/664faec2d53bbeab8968803f_How%20ChatGPT%20Supercharges%20Our%20Workflow%20at%20Setsail%20Marketing.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/673f61ea199b36e53af70408_pre.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/64738f23ff1a5e8927488653_image%20(2).avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/6427385a5c4c4c05cf324f13_Setsail%20Accessible%20Design.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/65ab1a606bbdaa898d815363_Setsail%20marketing%20adventure%20video%20marketing.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/65ab0d7cefb10eec3d6fd98d_cute-woman-genuinely-laughs-relaxing-on-beach-setsail-authentic-content-marketing.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/665166521c8dd2f6ad7f9493_SetsailBTS2.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/648f3f380f3d5c894fd26404_camera%203.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/64878e3fbb100df8a26938db_image.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/64aa217ec0f80ed7004641df_DSC00688%20(1).avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/644ea6668a6c7918d4394e31_steven-lelham-atSaEOeE8Nk-unsplash.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/664fc6bcb8f99be7224e4b39_Setsail%20Marketing%20on%20shoot.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/65ab30a910c617827f892df1_young-pair-with-perfect-figure-near-swimming-pool-Setsail%20marketing%20luxury%20travel.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/645fbefd224d3b1aafd8e6af_download.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/6456899769813c317bf36c3e_maxresdefault.avif",
                "https://cdn.prod.website-files.com/6401247271fb767251b81819/642a38f98205511cd5e90c06_john-schnobrich-FlPc9_VocJ4-unsplash.avif"
            ],
            social_links={
                "twitter": None,
                "linkedin": "https://www.linkedin.com/company/setsailmarketing/",
                "facebook": "https://www.facebook.com/yousetsail",
                "instagram": "https://www.instagram.com/setsailmkt/",
                "youtube": "https://www.youtube.com/channel/UCmGZmyMkczPcWDSoKiDP5jw",
                "tiktok": None
            },
            company_details={
                "founded": "2015",
                "employees": "10-49",
                "location": "Main studio at 200-1737 Boundary Rd, Vancouver, BC, Canada, with an additional office in Beaverton, Oregon; serving clients across Canada and the United States",
                "industry": "Digital marketing and advertising agency focused on performance marketing, PPC, SEO, social media, web design and development, branding, video production, and marketing automation (B Corp certified)"
            },
            questionnaire=[
                {"question": "Tone or voice to absolutely avoid", "answer": "Avoid anything that feels aggressive, arrogant, manipulative, overly salesy, generic/cookie-cutter, cold or unapproachable, overly technical/jargon-heavy, or stiff/corporate. The tone should never feel insincere or like \"hard sell.\""},
                {"question": "Personality traits the brand should never show", "answer": "Avoid coming across as arrogant, pushy, desperate, condescending, unprofessional, dishonest, flaky/indecisive, or apathetic. The brand should feel confident and grounded, not needy or ego-driven."},
                {"question": "Emotional responses we should never evoke", "answer": "Avoid content that leaves people feeling confused, overwhelmed, intimidated, shamed, offended, belittled, scared, or bored. If in doubt, steer toward clarity, empowerment, and calm confidence."},
                {"question": "Ways we should never position the company vs. competitors", "answer": "Avoid trash-talking competitors, making unfounded \"we're the best/only\" claims, comparing specific features or prices without proof, or sounding desperate for business (\"we'll do anything,\" \"we're cheaper than everyone\"). Focus on what we do well, not on putting others down."},
                {"question": "Claims about products/services we should never make", "answer": "Never use absolute guarantees or exaggerated promises, such as: \"Guaranteed results,\" \"risk-free,\" \"works for everyone,\" \"instant,\" or \"effortless.\" \"#1 in the world\" or similar superlatives without solid evidence. Stick to truthful, supportable claims."},
                {"question": "Benefits/outcomes we should never promise", "answer": "Avoid promising specific revenue, profit, health, or life outcomes (e.g., \"double your revenue in 30 days,\" \"cure,\" \"completely eliminate X\"), or exact timelines for success. Talk in terms of possibilities, trends, and typical experiences, not guaranteed outcomes."},
                {"question": "Achievements/credentials we should avoid mentioning", "answer": "Avoid highlighting: Certifications, awards, or partnerships that are pending, disputed, or outdated. Any third-party logos or endorsements without explicit permission. Internal or unofficial achievements that can't be externally verified."},
                {"question": "Specific words/phrases that should never appear", "answer": "Avoid: Low-value or low-quality language like \"cheap,\" \"dirt-cheap,\" \"bargain-bin.\" Words that insult or stereotype customers. Fear-mongering or manipulative phrases (\"only an idiot wouldn't…\"). Anything profane, explicit, or discriminatory."},
                {"question": "Acronyms/technical terms to avoid or always explain", "answer": "Avoid internal acronyms and niche technical jargon that the average customer wouldn't know. If an acronym or technical term is necessary, spell it out on first use and explain it in plain language."},
                {"question": "Corporate buzzwords/fluffy language to avoid", "answer": "Avoid overused buzzwords and vague phrases like: \"Synergy,\" \"game-changing,\" \"disruptive,\" \"cutting-edge,\" \"world-class,\" \"innovative solutions,\" \"paradigm shift,\" \"utilize\" (instead of \"use\"), etc. Prefer concrete, specific wording."},
                {"question": "Casual expressions/slang/informal terms to avoid", "answer": "Avoid trendy or potentially exclusionary slang, strong swearing, sexual innuendo, or anything that could feel unprofessional (\"lit,\" \"savage,\" \"WTF,\" etc.). Humor is fine, but slang should not undermine clarity or credibility."},
                {"question": "Pricing-related words to avoid", "answer": "Avoid language that cheapens the brand or invites haggling, such as \"cheap,\" \"dirt cheap,\" \"bargain,\" \"lowest price,\" or \"negotiable\" (unless that's a formal policy). Don't reference competitors' specific prices. Emphasize value and outcomes, not being \"the cheapest.\""},
                {"question": "Industry-specific topics/issues we should never address", "answer": "Avoid publicly commenting on: Active lawsuits, scandals, or investigations (ours or competitors'). Confidential trade practices or non-public industry information. Speculation about illegal or unethical behavior in the industry."},
                {"question": "Current events/news topics to avoid", "answer": "Avoid taking public positions on polarizing political issues, elections, wars, or highly sensitive societal conflicts unless leadership explicitly directs otherwise. We also avoid \"newsjacking\" tragedies or crises for marketing."},
                {"question": "Aspects of business operations that must remain confidential", "answer": "Keep private: Proprietary processes, algorithms, playbooks, and internal tools. Detailed financials (margins, internal rates, salaries). Non-public strategic plans, roadmaps, and negotiations. Internal conflicts, HR issues, or partner disagreements."},
                {"question": "Demographic groups/customer segments to be especially careful with", "answer": "Be especially cautious when speaking about or to: Minors and young people. Older adults, people with disabilities, and other vulnerable groups. Marginalized communities. Avoid stereotypes, \"poverty porn,\" or messaging that exploits vulnerability."},
                {"question": "Sensitive personal/professional topics", "answer": "Avoid presenting the brand as an authority on people's private struggles (health, mental health, trauma, addiction, finances, relationships, etc.). Don't speculate about or dramatize these topics, and never shame people for their circumstances."},
                {"question": "Cultural, religious, or social topics needing extreme caution", "answer": "Avoid using religious or cultural symbols, rituals, or language purely as aesthetic sales tools. Don't joke about or trivialize any culture, religion, or identity group. If referenced, handle with respect and neutrality, not as a marketing gimmick."},
                {"question": "Competitors that should never be mentioned", "answer": "Default: don't name competitors at all unless the client explicitly approves it and there's a clear strategy. When we do mention others, keep it factual and respectful."},
                {"question": "Comparative statements about competitors that are off-limits", "answer": "Avoid: \"We're better than X\" without proof. Direct performance, quality, or pricing comparisons that can't be substantiated. Misleading or out-of-context comparisons. When needed, focus on explaining our approach, not attacking others."},
                {"question": "Former business partners or relationships to avoid referencing", "answer": "Avoid mentioning past partners, employees, or clients if: There were disputes or unhappy endings. We don't have explicit permission to use their name. The relationship is confidential or sensitive."},
                {"question": "Industry practices/standards we should not criticize", "answer": "Avoid publicly attacking core industry standards, regulatory bodies, or broadly accepted practices, even if we do things differently. Instead, frame our approach as \"an alternative that works for [our customers]\" rather than \"everyone else is wrong.\""},
                {"question": "Regulatory/legal requirements affecting content", "answer": "Assume we must comply with: Advertising and consumer-protection laws (no deceptive or unsubstantiated claims). Privacy and data regulations (no sharing sensitive personal info). Any sector-specific rules (e.g., around medical, financial, or child-related content). When in doubt, keep claims modest, factual, and clearly non-diagnostic/non-prescriptive."},
                {"question": "Disclaimers/legal language that must accompany certain topics", "answer": "Include appropriate disclaimers when discussing results, health, finances, or professional advice, e.g.: \"Results vary; no guarantee of specific outcomes.\" \"For informational purposes only; not legal/financial/medical advice.\" \"Past performance does not guarantee future results.\""},
                {"question": "Medical, financial, or professional advice we must never appear to provide", "answer": "We should never: Diagnose, treat, or prescribe for medical or mental-health conditions. Offer personalized financial, legal, or tax advice. Present ourselves as licensed professionals unless we actually are and the client has explicitly approved it. We can be educational and general, not advisory or prescriptive."},
                {"question": "Copyright, trademark, or IP concerns", "answer": "Avoid: Using third-party logos, artwork, or photos without a license or permission. Copying competitors' wording, layouts, or proprietary frameworks. Using trademarked names generically or without proper marks/attribution."},
                {"question": "Types of statistics/studies/data sources to avoid", "answer": "Avoid citing: Unsourced stats (\"studies show…\") or anonymous \"research says.\" Obvious low-credibility or biased sources. Tiny or non-representative studies presented as universal truth. Always prefer reputable, verifiable data with clear attribution."},
                {"question": "Level of scientific/factual claims we are not authorized to make", "answer": "We should not make strong causal or \"clinically proven\" claims unless there is clear, high-quality evidence and legal approval. Default to moderate language (\"may help,\" \"is associated with,\" \"many customers report…\") instead of \"will,\" \"cures,\" or \"eliminates.\""},
                {"question": "Testimonials/case studies/customer examples we should never reference", "answer": "Only use testimonials or case studies that: Have explicit written permission. Don't reveal sensitive personal or business information. Don't promise extreme or atypical results as if they are typical. If unsure, anonymize details or don't use the example."},
                {"question": "Business practices/industry approaches that conflict with values", "answer": "Avoid endorsing or aligning with: Exploitative labor, discrimination, or harassment. Dishonest or deceptive selling practices. Environmental harm as a \"necessary cost of doing business.\" Our content should reflect integrity, respect, and long-term responsibility."},
                {"question": "Social/environmental topics with a specific stance to respect", "answer": "Default stance: pro-inclusion and pro-responsibility. Avoid: Language that could be interpreted as discriminatory or dismissive. Greenwashing or exaggerated sustainability claims. If we mention social or environmental impact, keep it modest, factual, and aligned with actual practices."},
                {"question": "Partnerships/sponsorships/associations to avoid suggesting", "answer": "Avoid implying or suggesting partnerships with: Political parties or candidates. Adult, gambling, weapons, tobacco/vaping, or similar high-risk industries. Organizations known for unethical or controversial practices. Also, don't casually suggest \"partnering with X\" if there's no real relationship."},
                {"question": "Charitable causes/social issues that could be controversial", "answer": "Avoid tying the brand to highly polarizing or partisan causes unless it's a deliberate, approved choice. Default to broadly accepted, non-controversial causes if charity is mentioned at all."},
                {"question": "Internal processes/procedures that should never be detailed publicly", "answer": "Don't share: Detailed internal SOPs, review flows, security practices, or escalation procedures. Internal decision-making criteria, risk thresholds, or approval paths. Anything that could expose vulnerabilities or give competitors a playbook."},
                {"question": "Tools, software, or vendors we should avoid mentioning", "answer": "Avoid name-dropping specific vendors, tools, or platforms if: We don't actually use them or endorse them. They're competitors of core partners. There's any legal or contractual restriction on using their name in marketing. Default to generic descriptors (\"project management tool,\" \"CRM\") unless the client says otherwise."},
                {"question": "Pricing structures/packages/service details that are confidential", "answer": "Keep non-public pricing confidential: Custom quotes, discounts, or special deals. Internal cost breakdowns or margin details. Negotiation levers and minimums. Only mention pricing that's already publicly listed or explicitly approved."},
                {"question": "Geographic markets/customer types to avoid targeting", "answer": "Avoid creating content that directly targets: Regions where the company cannot legally operate or support customers. Countries or segments restricted by regulation, sanctions, or company policy. Extremely vulnerable groups where targeted marketing would be unethical."},
                {"question": "Content formats/structures to avoid", "answer": "Avoid formats that: Feel like clickbait or over-sensationalize serious topics. Over-promise with minimal substance (\"thin\" listicles with no depth). Trivialize complex issues that require nuance. Stick to formats that allow for clarity, context, and real value."},
                {"question": "Visual elements/examples/metaphors to avoid", "answer": "Avoid: Violent, sexualized, or discriminatory imagery. Stereotypical depictions of any demographic group. Appropriative use of religious or cultural symbols. Before/after visuals that imply unrealistic or guaranteed transformations."},
                {"question": "Call-to-action language/approaches that are inappropriate", "answer": "Avoid high-pressure or guilt-based CTAs like: \"Don't miss out or you'll regret it,\" \"Only an idiot wouldn't…,\" fake countdowns, or manufactured scarcity. CTAs should be clear, honest invitations, not emotional manipulation."},
                {"question": "Sources/publication types we should never link to", "answer": "Avoid linking to: Gossip sites, conspiracy blogs, or obvious misinformation sources. Hate-based or discriminatory outlets. Extremely low-credibility or spammy sites. When possible, favor reputable, neutral sources (known news outlets, peer-reviewed research, official organizations)."}
            ],
            existing_blog_titles=[
                "Podcast: How We Choose the Right Ad Platform: My Proven Framework for Google Ads vs. Facebook Ads",
                "Ecommerce Trends That Actually Matter: How to Spot What's Real Before Everyone Else",
                "Secrets to High-Quality Leads: A Podcast on Proven Digital Marketing Agency Strategies",
                "The AI-Powered SEO Advantage: How We're Winning in the Age of Search 3.0",
                "Podcast: How Do I Know If My Marketing Is Actually Working? (and How to Fix It)",
                "Your Website Is Still Your #1 Money-Maker – Here's Why",
                "How ChatGPT Supercharges Our Workflow at Setsail Marketing",
                "How to Use Social Media and Advertising to Grow Your Brand",
                "Setsail's Journey to Becoming a B Corp: A Reflection on our Commitment to Sustainability and Social Responsibility",
                "Inclusive and Accessible Design: Building Digital Experiences for Everyone",
                "Capturing the Adventure Spirit: How Video Elevates Adventure Brands & Destination Organizations",
                "The ROI of Authenticity: How Genuine Content Transforms Adventure Marketing",
                "Content Marketing for ourselves at Setsail Marketing",
                "Innovation in Digital Marketing: Setsail's 3D Adventure with DŌST Bikes' Crate Cargo Cruiser",
                "Embarking on a B-Corp Journey: How DŌST Bikes Sparked Setsail's Transformation",
                "Celebrating B Corp Certification: Insights from Setsail's Happy Hour Event",
                "5 Must-Haves for a Winning Government RFP Submission",
                "Elevating Every Customer Touchpoint at Setsail Marketing",
                "Nurturing Connections in Luxury Travel: The Video Storytelling Revolution",
                "Navigating the Branding Seas: Five Essential Principles from Our Voyage with Steepe & Co.",
                "Going the Distance: How DŌST Bikes' Record-Breaking Adventure Showcases the Impact of Storytelling in the Digital Age",
                "5 Signs Your Business Needs a Website Redesign: Is It Time for a Change?"
            ],
            ready=True,
            created_at=datetime.fromisoformat("2025-11-21T23:56:54.547962"),
            updated_at=datetime.fromisoformat("2025-11-25T20:57:16.656304"),
        )
    elif client_id == 7:
        # Real CleanDesign.ca data from production database
        from datetime import datetime
        return ClientContextRead(
            id=7,
            client_id=7,
            domain="cleandesign.ca",
            call_to_action="Explore Our Solutions",
            about="CleanDesign is a Canadian clean technology company specializing in hybrid energy management systems (hEMS) that integrate battery energy storage, intelligent software, and automated power management to optimize high-demand, mission‑critical operations. Their systems are designed to reduce fuel consumption, greenhouse gas emissions, and operational downtime for applications such as oil and gas drilling rigs, mining operations, remote and off‑grid communities, and EV charging infrastructure. CleanDesign's proprietary controls and AI‑enabled software dynamically balance loads across generators and batteries, enabling load‑dependent starting, peak shaving, blackout reduction, and predictive maintenance. By gathering millisecond‑level operational data and applying machine learning, hEMS continuously improves performance over time, delivering measurable outcomes like millions of dollars in annual fuel savings, tens of thousands of tonnes of CO₂ reductions, and significantly fewer maintenance events. The company positions itself as a partner to both operators and investors, manufacturing and deploying cash‑generating hEMS units that help customers meet ESG and sustainability targets while improving reliability and total cost of ownership.",
            competitors=[
                "Aggreko (hybrid power and energy storage)",
                "Wärtsilä (hybrid and energy storage systems)",
                "Caterpillar / Cat Hybrid Microgrid Solutions",
                "Schneider Electric (EcoStruxure Microgrid and energy management)",
                "ABB Ability Microgrids",
                "E.ON / Siemens Energy hybrid microgrid and storage providers",
                "other industrial battery energy storage and hybrid power system integrators serving oil & gas",
                "mining",
                "remote communities",
                "and EV charging infrastructure."
            ],
            brand_pov="Modern high‑power operations shouldn't have to choose between reliability, cost efficiency, and decarbonization. CleanDesign's point of view is that traditional diesel‑only power setups are fundamentally inefficient—running multiple gensets at partial load wastes fuel, increases emissions, and drives up maintenance and downtime. Instead of incremental optimizations, they advocate for a system‑level, software‑driven approach where batteries, generators, and intelligent controls work together as a hybrid energy management system. Their stance is that the value of clean technology must be proven in hard numbers—fuel saved, CO₂ reduced, downtime avoided, and payback achieved—so they design hEMS around clear, quantifiable outcomes that can 'pay for themselves' in demanding industrial environments. By translating complex engineering into simple, benefit‑driven solutions and wrapping it in a credible, modern brand, CleanDesign positions itself as a trusted partner helping operators and investors achieve both ESG goals and superior operational performance.",
            ideal_target_market="Operators and owners of high‑power, mission‑critical assets who face high fuel costs, emissions pressure, and grid limitations, including: (1) drilling contractors and oil & gas operators running land rigs that depend on diesel gensets and experience low‑load inefficiencies, high maintenance, and emissions scrutiny; (2) mining companies and remote industrial sites that require reliable continuous power, often in locations with weak or no grid access; (3) remote and off‑grid communities and critical infrastructure operators seeking to reduce diesel dependence and improve sustainability while maintaining reliability; and (4) EV charging network operators and fleet depots constrained by grid capacity who need to serve many fast chargers or heavy‑duty vehicles without costly grid upgrades. Best‑fit customers view energy as a strategic lever, care about ESG and regulatory compliance, and are willing to invest in hybrid energy systems that deliver measurable ROI, reduced emissions, and higher uptime rather than simply minimizing upfront equipment costs.",
            brand_safety={
                "disallowed_tones": [
                    "Over-hyped, promotional language that feels like a \"get rich quick\" or \"silver bullet\" solution.",
                    "Fear-based, alarmist, or shaming messaging about emissions, climate, or operational risk.",
                    "Overly casual or jokey tone that undermines the seriousness of industrial operations and safety.",
                    "Hostile, polarizing, or partisan political language (especially around energy policy).",
                    "Language that suggests disregard for community, environmental, or worker safety concerns."
                ],
                "disallowed_claims": [
                    "Unqualified guarantees of financial outcomes (e.g., \"we guarantee you'll save $6M+ per year\").",
                    "Specific performance or emissions-reduction numbers without data, context, or assumptions.",
                    "Claims of regulatory compliance or certification that are not formally granted or documented.",
                    "Statements implying the technology is entirely risk-free or maintenance-free.",
                    "Assertions of being the \"only\" or \"number one\" solution in the market without independent evidence."
                ],
                "sensitive_topics": [
                    "Partisan political commentary, campaigning, or endorsements (including on board members' prior political roles).",
                    "Health or medical promises related to emissions reductions (e.g., implying treatment or cure of diseases).",
                    "Investment or securities advice, including promises of returns to shareholders or investors.",
                    "Content that appears to greenwash high-emission operations without acknowledging tradeoffs and data.",
                    "Any depiction of unsafe industrial practices or minimization of safety and environmental regulations."
                ]
            },
            author_tone="Technical but accessible, data-driven, sustainability-focused, B2B-professional, confident yet measured, focused on operational reliability and ROI.",
            author_rules=[
                "Lead with clear, benefit-focused language that ties hEMS technology to tangible outcomes like fuel savings, reduced downtime, and lower emissions.",
                "Translate engineering complexity into plain, accurate language that non-technical decision-makers can understand, while still feeling credible to engineers.",
                "Use data and quantified results (e.g., savings, CO2 reduction) only when you can reference real deployments, timeframes, and assumptions.",
                "Avoid absolute guarantees; phrase impact as \"expected\", \"based on deployments\", or \"modeled\" and provide context where possible.",
                "Emphasize safety, reliability, and continuity of operations whenever discussing system performance in high-stakes environments.",
                "Frame sustainability as both an environmental and economic advantage (emissions reduction plus fuel and maintenance savings).",
                "Stay respectful and neutral when referencing oil & gas, mining, or remote communities; focus on partnership and performance, not judgment.",
                "Keep the writing concise and structured (short paragraphs, clear headings, bullet points for key stats or benefits).",
                "Avoid buzzwords and vague claims; back up statements with specifics such as use cases, sectors, or operational scenarios.",
                "Maintain a consistent, confident voice that reflects an established industrial technology partner rather than an early-stage speculative startup."
            ],
            logos=[
                "https://cdn.prod.website-files.com/66ecb5e5dbe444d134d5a8b5/6723b5dd8f42c311c0f69883_Logo%20Coloured.svg",
                "https://cdn.prod.website-files.com/66ecb5e5dbe444d134d5a8b5/6723b6354a0c0139563a3145_Logo_white.svg"
            ],
            colors=[
                "#021529",
                "#00C7A5",
                "#F5F5F5"
            ],
            fonts=[
                "Clean",
                "modern sans-serif (likely Inter or similar)",
                "with system fallbacks such as -apple-system",
                "BlinkMacSystemFont",
                "\"Segoe UI\"",
                "sans-serif"
            ],
            images_used=None,
            social_links={
                "twitter": None,
                "linkedin": "https://www.linkedin.com/company/cleandesign-inc/",
                "facebook": None,
                "instagram": None,
                "youtube": None,
                "tiktok": None
            },
            company_details={
                "founded": "2017",
                "employees": "10-50",
                "location": "Headquartered in Toronto, Ontario, Canada (with operations focused on North American and other high‑power industrial and remote markets)",
                "industry": "Clean technology; energy management and engineering; hybrid energy management systems; battery energy storage and power optimization for industrial, oil & gas, mining, remote communities, and EV charging infrastructure."
            },
            questionnaire=[
                {"question": "Tone or voice to absolutely avoid", "answer": "Avoid anything that feels aggressive, arrogant, manipulative, overly salesy, generic/cookie-cutter, cold or unapproachable, overly technical/jargon-heavy, or stiff/corporate. The tone should never feel insincere or like \"hard sell.\""},
                {"question": "Personality traits the brand should never show", "answer": "Avoid coming across as arrogant, pushy, desperate, condescending, unprofessional, dishonest, flaky/indecisive, or apathetic. The brand should feel confident and grounded, not needy or ego-driven."},
                {"question": "Emotional responses we should never evoke", "answer": "Avoid content that leaves people feeling confused, overwhelmed, intimidated, shamed, offended, belittled, scared, or bored. If in doubt, steer toward clarity, empowerment, and calm confidence."},
                {"question": "Ways we should never position the company vs. competitors", "answer": "Avoid trash-talking competitors, making unfounded \"we're the best/only\" claims, comparing specific features or prices without proof, or sounding desperate for business (\"we'll do anything,\" \"we're cheaper than everyone\"). Focus on what we do well, not on putting others down."},
                {"question": "Claims about products/services we should never make", "answer": "Never use absolute guarantees or exaggerated promises, such as: \"Guaranteed results,\" \"risk-free,\" \"works for everyone,\" \"instant,\" or \"effortless.\" \"#1 in the world\" or similar superlatives without solid evidence. Stick to truthful, supportable claims."},
                {"question": "Benefits/outcomes we should never promise", "answer": "Avoid promising specific revenue, profit, health, or life outcomes (e.g., \"double your revenue in 30 days,\" \"cure,\" \"completely eliminate X\"), or exact timelines for success. Talk in terms of possibilities, trends, and typical experiences, not guaranteed outcomes."},
                {"question": "Achievements/credentials we should avoid mentioning", "answer": "Avoid highlighting: Certifications, awards, or partnerships that are pending, disputed, or outdated. Any third-party logos or endorsements without explicit permission. Internal or unofficial achievements that can't be externally verified."},
                {"question": "Specific words/phrases that should never appear", "answer": "Avoid: Low-value or low-quality language like \"cheap,\" \"dirt-cheap,\" \"bargain-bin.\" Words that insult or stereotype customers. Fear-mongering or manipulative phrases (\"only an idiot wouldn't…\"). Anything profane, explicit, or discriminatory."},
                {"question": "Acronyms/technical terms to avoid or always explain", "answer": "Avoid internal acronyms and niche technical jargon that the average customer wouldn't know. If an acronym or technical term is necessary, spell it out on first use and explain it in plain language."},
                {"question": "Corporate buzzwords/fluffy language to avoid", "answer": "Avoid overused buzzwords and vague phrases like: \"Synergy,\" \"game-changing,\" \"disruptive,\" \"cutting-edge,\" \"world-class,\" \"innovative solutions,\" \"paradigm shift,\" \"utilize\" (instead of \"use\"), etc. Prefer concrete, specific wording."},
                {"question": "Casual expressions/slang/informal terms to avoid", "answer": "Avoid trendy or potentially exclusionary slang, strong swearing, sexual innuendo, or anything that could feel unprofessional (\"lit,\" \"savage,\" \"WTF,\" etc.). Humor is fine, but slang should not undermine clarity or credibility."},
                {"question": "Pricing-related words to avoid", "answer": "Avoid language that cheapens the brand or invites haggling, such as \"cheap,\" \"dirt cheap,\" \"bargain,\" \"lowest price,\" or \"negotiable\" (unless that's a formal policy). Don't reference competitors' specific prices. Emphasize value and outcomes, not being \"the cheapest.\""},
                {"question": "Industry-specific topics/issues we should never address", "answer": "Avoid publicly commenting on: Active lawsuits, scandals, or investigations (ours or competitors'). Confidential trade practices or non-public industry information. Speculation about illegal or unethical behavior in the industry."},
                {"question": "Current events/news topics to avoid", "answer": "Avoid taking public positions on polarizing political issues, elections, wars, or highly sensitive societal conflicts unless leadership explicitly directs otherwise. We also avoid \"newsjacking\" tragedies or crises for marketing."},
                {"question": "Aspects of business operations that must remain confidential", "answer": "Keep private: Proprietary processes, algorithms, playbooks, and internal tools. Detailed financials (margins, internal rates, salaries). Non-public strategic plans, roadmaps, and negotiations. Internal conflicts, HR issues, or partner disagreements."},
                {"question": "Demographic groups/customer segments to be especially careful with", "answer": "Be especially cautious when speaking about or to: Minors and young people. Older adults, people with disabilities, and other vulnerable groups. Marginalized communities. Avoid stereotypes, \"poverty porn,\" or messaging that exploits vulnerability."},
                {"question": "Sensitive personal/professional topics", "answer": "Avoid presenting the brand as an authority on people's private struggles (health, mental health, trauma, addiction, finances, relationships, etc.). Don't speculate about or dramatize these topics, and never shame people for their circumstances."},
                {"question": "Cultural, religious, or social topics needing extreme caution", "answer": "Avoid using religious or cultural symbols, rituals, or language purely as aesthetic sales tools. Don't joke about or trivialize any culture, religion, or identity group. If referenced, handle with respect and neutrality, not as a marketing gimmick."},
                {"question": "Competitors that should never be mentioned", "answer": "Default: don't name competitors at all unless the client explicitly approves it and there's a clear strategy. When we do mention others, keep it factual and respectful."},
                {"question": "Comparative statements about competitors that are off-limits", "answer": "Avoid: \"We're better than X\" without proof. Direct performance, quality, or pricing comparisons that can't be substantiated. Misleading or out-of-context comparisons. When needed, focus on explaining our approach, not attacking others."},
                {"question": "Former business partners or relationships to avoid referencing", "answer": "Avoid mentioning past partners, employees, or clients if: There were disputes or unhappy endings. We don't have explicit permission to use their name. The relationship is confidential or sensitive."},
                {"question": "Industry practices/standards we should not criticize", "answer": "Avoid publicly attacking core industry standards, regulatory bodies, or broadly accepted practices, even if we do things differently. Instead, frame our approach as \"an alternative that works for [our customers]\" rather than \"everyone else is wrong.\""},
                {"question": "Regulatory/legal requirements affecting content", "answer": "Assume we must comply with: Advertising and consumer-protection laws (no deceptive or unsubstantiated claims). Privacy and data regulations (no sharing sensitive personal info). Any sector-specific rules (e.g., around medical, financial, or child-related content). When in doubt, keep claims modest, factual, and clearly non-diagnostic/non-prescriptive."},
                {"question": "Disclaimers/legal language that must accompany certain topics", "answer": "Include appropriate disclaimers when discussing results, health, finances, or professional advice, e.g.: \"Results vary; no guarantee of specific outcomes.\" \"For informational purposes only; not legal/financial/medical advice.\" \"Past performance does not guarantee future results.\""},
                {"question": "Medical, financial, or professional advice we must never appear to provide", "answer": "We should never: Diagnose, treat, or prescribe for medical or mental-health conditions. Offer personalized financial, legal, or tax advice. Present ourselves as licensed professionals unless we actually are and the client has explicitly approved it. We can be educational and general, not advisory or prescriptive."},
                {"question": "Copyright, trademark, or IP concerns", "answer": "Avoid: Using third-party logos, artwork, or photos without a license or permission. Copying competitors' wording, layouts, or proprietary frameworks. Using trademarked names generically or without proper marks/attribution."},
                {"question": "Types of statistics/studies/data sources to avoid", "answer": "Avoid citing: Unsourced stats (\"studies show…\") or anonymous \"research says.\" Obvious low-credibility or biased sources. Tiny or non-representative studies presented as universal truth. Always prefer reputable, verifiable data with clear attribution."},
                {"question": "Level of scientific/factual claims we are not authorized to make", "answer": "We should not make strong causal or \"clinically proven\" claims unless there is clear, high-quality evidence and legal approval. Default to moderate language (\"may help,\" \"is associated with,\" \"many customers report…\") instead of \"will,\" \"cures,\" or \"eliminates.\""},
                {"question": "Testimonials/case studies/customer examples we should never reference", "answer": "Only use testimonials or case studies that: Have explicit written permission. Don't reveal sensitive personal or business information. Don't promise extreme or atypical results as if they are typical. If unsure, anonymize details or don't use the example."},
                {"question": "Business practices/industry approaches that conflict with values", "answer": "Avoid endorsing or aligning with: Exploitative labor, discrimination, or harassment. Dishonest or deceptive selling practices. Environmental harm as a \"necessary cost of doing business.\" Our content should reflect integrity, respect, and long-term responsibility."},
                {"question": "Social/environmental topics with a specific stance to respect", "answer": "Default stance: pro-inclusion and pro-responsibility. Avoid: Language that could be interpreted as discriminatory or dismissive. Greenwashing or exaggerated sustainability claims. If we mention social or environmental impact, keep it modest, factual, and aligned with actual practices."},
                {"question": "Partnerships/sponsorships/associations to avoid suggesting", "answer": "Avoid implying or suggesting partnerships with: Political parties or candidates. Adult, gambling, weapons, tobacco/vaping, or similar high-risk industries. Organizations known for unethical or controversial practices. Also, don't casually suggest \"partnering with X\" if there's no real relationship."},
                {"question": "Charitable causes/social issues that could be controversial", "answer": "Avoid tying the brand to highly polarizing or partisan causes unless it's a deliberate, approved choice. Default to broadly accepted, non-controversial causes if charity is mentioned at all."},
                {"question": "Internal processes/procedures that should never be detailed publicly", "answer": "Don't share: Detailed internal SOPs, review flows, security practices, or escalation procedures. Internal decision-making criteria, risk thresholds, or approval paths. Anything that could expose vulnerabilities or give competitors a playbook."},
                {"question": "Tools, software, or vendors we should avoid mentioning", "answer": "Avoid name-dropping specific vendors, tools, or platforms if: We don't actually use them or endorse them. They're competitors of core partners. There's any legal or contractual restriction on using their name in marketing. Default to generic descriptors (\"project management tool,\" \"CRM\") unless the client says otherwise."},
                {"question": "Pricing structures/packages/service details that are confidential", "answer": "Keep non-public pricing confidential: Custom quotes, discounts, or special deals. Internal cost breakdowns or margin details. Negotiation levers and minimums. Only mention pricing that's already publicly listed or explicitly approved."},
                {"question": "Geographic markets/customer types to avoid targeting", "answer": "Avoid creating content that directly targets: Regions where the company cannot legally operate or support customers. Countries or segments restricted by regulation, sanctions, or company policy. Extremely vulnerable groups where targeted marketing would be unethical."},
                {"question": "Content formats/structures to avoid", "answer": "Avoid formats that: Feel like clickbait or over-sensationalize serious topics. Over-promise with minimal substance (\"thin\" listicles with no depth). Trivialize complex issues that require nuance. Stick to formats that allow for clarity, context, and real value."},
                {"question": "Visual elements/examples/metaphors to avoid", "answer": "Avoid: Violent, sexualized, or discriminatory imagery. Stereotypical depictions of any demographic group. Appropriative use of religious or cultural symbols. Before/after visuals that imply unrealistic or guaranteed transformations."},
                {"question": "Call-to-action language/approaches that are inappropriate", "answer": "Avoid high-pressure or guilt-based CTAs like: \"Don't miss out or you'll regret it,\" \"Only an idiot wouldn't…,\" fake countdowns, or manufactured scarcity. CTAs should be clear, honest invitations, not emotional manipulation."},
                {"question": "Sources/publication types we should never link to", "answer": "Avoid linking to: Gossip sites, conspiracy blogs, or obvious misinformation sources. Hate-based or discriminatory outlets. Extremely low-credibility or spammy sites. When possible, favor reputable, neutral sources (known news outlets, peer-reviewed research, official organizations)."}
            ],
            existing_blog_titles=[
                "CleanDesign Announces Name Change and New Board Member"
            ],
            ready=True,
            created_at=datetime.fromisoformat("2025-11-24T21:56:03.571957"),
            updated_at=datetime.fromisoformat("2025-11-24T21:56:03.571963"),
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

