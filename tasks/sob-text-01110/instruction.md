Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
16th World Economic Forum on Africa: The 16th World Economic Forum on Africa: Going for Growth was a World Economic Forum economic summit meeting held in Cape Town, South Africa, from May 31 to June 2, 2006.  The summit was attended by some 650 political and business leaders from 39 countries, focusing particularly on rapidly increasing African commodity prices.  It also examined issues relating to the promotion of investment, improving world opinion, combating hunger, sustainable development, and offer specific initiatives to address these and other economic issues facing part of or the entire continent.

World Social Forum: The World Social Forum (WSF, Portuguese: "Fórum Social Mundial" ] ) is an annual meeting of civil society organizations, first held in Brazil, which offers a self-conscious effort to develop an alternative future through the championing of counter-hegemonic globalization.  The World Social Forum can be considered a visible manifestation of global civil society, bringing together non governmental organizations, advocacy campaigns, and formal and informal social movements seeking international solidarity.  The World Social Forum prefers to define itself as "an opened space – plural, diverse, non-governmental and non-partisan – that stimulates the decentralized debate, reflection, proposals building, experiences exchange and alliances among movements and organizations engaged in concrete actions towards a more solidarity, democratic and fair world...a permanent space and process to build alternatives to neoliberalism."  It is held by members of the alter-globalization movement (also referred to as the global justice movement) who come together to coordinate global campaigns, share and refine organizing strategies, and inform each other about movements from around the world and their particular issues.  The World Social Forum is explicit about not being a representative of all of those who attend and thus does not publish any formal statements on behalf of participants.  It tends to meet in January at the same time as its "great capitalist rival", the World Economic Forum's Annual Meeting in Davos, Switzerland.  This date is consciously picked to promote alternative answers to world economic problems in opposition to the World Economic Forum.

Summer Palace Dialogue: The Summer Palace Dialogue (SPD) is an economic forum which brings together economists from both China and the United States to discuss economic cooperation between the two largest economies in the world.  SPD is co-hosted by Chinese Economists 50 Forum and the Columbia Global Centers East Asia, and was formerly co-hosted by the Brookings Institution.  It was founded in 2009 by former Vice Chairman of the Joint Chiefs of Staff and current Chairman of AEA Investors Admiral Bill Owens and Vice Minister Liu He of the Chinese Central Leading Group on Financial and Economic Affairs.  The forum extends for two days.  Participants spend the first day in private discussions and then convene a half-day public session to summarize their observations, analyses, and conclusions with the press and a broader audience.  The Summer Palace Dialogue is scheduled annually in mid-September in Beijing, right before the Summer World Economic Forum in Dalian.  The third annual Summer Palace Dialogue was held on September 12–13, 2011.

Perrott-Warrick Fund: The Perrot–Warrick Fund is administered by Trinity College, Cambridge, and awards grants for research in parapsychology.  According to Susan Blackmore, it is the second largest source of grants for psychical research in the UK, after the University of Edinburgh's Koestler Parapsychology Unit.  Caroline Watt of the University of Edinburgh has been Perrott–Warrick Senior Researcher since 2010.  The position was previously held by Rupert Sheldrake, Richard Wiseman and Nicholas Humphrey.

1976 Democratic National Convention: The 1976 Democratic National Convention met at Madison Square Garden in New York City, from July 12 to July 15, 1976.  The assembled United States Democratic Party delegates at the convention nominated former Governor Jimmy Carter of Georgia for President and Senator Walter Mondale of Minnesota for Vice President.  John Glenn and Barbara Jordan gave the keynote addresses.  Jordan's keynote address made her the first African-American woman to deliver the keynote address at a Democratic National Convention.  It was listed as #5 in American Rhetoric's Top 100 Speeches of the 20th Century (listed by rank).  The convention was the first in New York City since the 103-ballot 1924 convention.

Young Global Leaders: The Young Global Leaders, or Forum of Young Global Leaders, is an independent non-profit organization managed from Geneva, Switzerland, under the supervision of the Swiss government.  Launched by Klaus Schwab of the World Economic Forum in 2004, the Young Global Leaders are governed by a board of twelve world and industry leaders, ranging from Queen Rania of Jordan to Marissa Mayer of Yahoo! and Wikipedia co-founder Jimmy Wales.  Schwab created the group with $1 million won from the Dan David Prize, and the inaugural 2005 class comprised 237 young leaders.  Young Global Leaders participate in the Annual Meeting of the New Champions, established in 2007 and known informally as "Summer Davos", alongside Global Growth Companies and other delegations to the World Economic Forum.

Jeremy Howard (entrepreneur): Jeremy Howard (born 13 November 1973) is an Australian data scientist and entrepreneur.  He is a founding researcher at fast.ai, a research institute dedicated to make Deep Learning more accessible.  Previously, he was the CEO and Founder at Enlitic, an advanced machine learning company in San Francisco, California.  Prior to it, Howard was the President and Chief Scientist at Kaggle, a community and competition platform of over 200,000 data scientists.  Howard is the youngest faculty member at Singularity University, where he teaches data science.  He is also a Young Global Leader with the World Economic Forum, and spoke at the World Economic Forum Annual Meeting 2014 on "Jobs For The Machines."  Howard advised Khosla Ventures as their Data Strategist, identifying the biggest opportunities for investing in data-driven startups and mentoring their portfolio companies to build data-driven businesses.  Howard was the founding CEO of two successful Australian startups, FastMail and Optimal Decisions Group.  Before that, he spent eight years in management consulting, at McKinsey & Company and AT Kearney.

Global Irish Economic Forum: The Global Irish Economic Forum is a biennial conference held in Dublin, Ireland.  Inspired by the World Economic Forum in Switzerland, international figures from the worlds of business and culture attend the event.  The first Forum was held at Farmleigh in Dublin's Phoenix Park from 18–20 September 2009, and was given widespread coverage by RTÉ.  The second forum was held at Dublin Castle in 2011.

Jeddah Economic Forum: Jeddah Economic Forum (JEF) (Arabic: منتدى جدة الإقتصادي) is a forum held annually since 1999 during winter in Jeddah, western Saudi Arabia.  It has become the region's Middle East strategic think tank focusing on regional and international economic and social issues.  The Jeddah Economic Forum is organized by the Jeddah Marketing Board, which is a part of Jeddah Chamber of Commerce & Industry.

Richard Wiseman: Richard J. Wiseman (born 1966) is a Professor of the Public Understanding of Psychology at the University of Hertfordshire in the United Kingdom.  He has written several best-selling popular psychology books that have been translated into over 30 languages.  He has given keynote addresses to The Royal Society, The Swiss Economic Forum, Google and Amazon.  He is a fellow for the Committee for Skeptical Inquiry and a patron of the British Humanist Association.

Question: Which Perrot-Warrick Senior Researcher has also given keynote addresses at The Swiss Economic Forum?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual who meets the criteria."
    },
    "is_perrott_warrick_senior_researcher": {
      "type": "boolean",
      "description": "True if the person held the Perrott-Warrick Senior Researcher position."
    },
    "is_swiss_economic_forum_keynote_speaker": {
      "type": "boolean",
      "description": "True if the person gave a keynote address at The Swiss Economic Forum."
    },
    "other_keynote_venues": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other organizations or events where the person gave keynote addresses, if mentioned."
    }
  },
  "required": [
    "person_name",
    "is_perrott_warrick_senior_researcher",
    "is_swiss_economic_forum_keynote_speaker"
  ],
  "additionalProperties": false
}
