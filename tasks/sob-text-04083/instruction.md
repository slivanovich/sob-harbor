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
Guelph Community Health Centre: The Guelph Community Health Centre (Guelph CHC, GCHC) is a public, non-profit organization that provides primary health care to the community of Guelph, Ontario, Canada, as well as a variety of programs that focus on holistic health promotion and community development.  The Guelph CHC is a member of the Association of Ontario Health Centres (AOHC) and one of over 300 CHCs in Canada.  The Guelph CHC has one main location in downtown Guelph, as well as a satellite clinic located on Shelldale Crescent, and an Early Years Satellite location, situated in the Stone Road Mall.

Rejuvelac: Rejuvelac is kind of grain water invented and promoted by Ann Wigmore.

Victor Stancarone: Victor "Sonny" Stancarone is an American Internet personality, holistic health & wellness teacher, improvisational jazz pianist, and graduate from Adelphi University.  A former yoga teacher and exercise physiologist, he promotes piano playing for health & well-being through his website "SonnysPianoTV.com", instructional DVD kit, and Internet show "Sonny's Piano TV Show", which also airs on Long Island Cablevision public-access television cable TV.

Kripalu Center: The Kripalu Center for Yoga & Health is a non-profit organization that operates a health and yoga retreat in Stockbridge, Massachusetts.  Its 160000 ft2 facility is a former Jesuit novitiate and juniorate seminary built in 1957.  The center has described itself as North America's largest residential facility for holistic health and education.  With 2013 revenue of $34.7 million, it employed about 626 people as of 2008 and can accommodate more than 650 overnight guests.

Ann Wigmore: Ann Wigmore (1909–1994) was a Lithuanian–American "holistic health" practitioner and raw food advocate.  Wigmore wrote several books on her theories and lectured widely to promote her practices.

Mercy Medical Center (Springfield, Massachusetts): Mercy Medical Center (also known as Mercy Medical, or Mercy Hospital,) is located in Springfield, Massachusetts.  Run by the Sisters of Providence Health System, Mercy Hospital is a faith-based, non-profit organization serving patients regardless of background or beliefs.  Mercy Medical Center is known for its tradition of holistic health care.

Mickey Mehta: Mickey Mehta (born 29 August 1962) is an Indian holistic health, well-being, wellness, and fitness guru.  He is a TV and radio presenter (94.3 Radio One Mumbai and Delhi) and a columnist in various publications and websites.  He preaches the concept of holistic health and equipment free workouts and has done so by establishing a chain of Mickey Mehta Wellness Temples across Mumbai city.  The media often refer to Mickey Mehta as 'India's Leading Holistic Health Guru'.  Mehta also aspires to build the largest social media base across as many platforms possible, to reach out to his audience.

Viktoras Kulvinskas: Viktoras Peter Kulvinskas (born 23 February 1939) is a Lithuanian holistic health practitioner, nutritionist, raw foods advocate and author.

Anna Lappé: Anna Lappé is an author and educator, known for her work as an expert on food systems and as a sustainable food advocate.  The co-author or author of three books and the contributing author to over ten others, Anna's work has been widely translated internationally and featured in "The New York Times", "Gourmet", "O, The Oprah Magazine", "Domino", "Food & Wine", "Body+Soul", "Natural Health", "Utne Reader", and "Vibe", among other outlets.  With her mother Frances Moore Lappé, Anna co-founded the Cambridge-based Small Planet Institute, an international network for research and popular education about the root causes of hunger and poverty.  The Lappés are also co-founders of the Small Planet Fund, which has raised nearly $1 million for democratic social movements worldwide, two of which have won the Nobel Peace Prize since the Fund's founding in 2002.  Anna's research on sustainable agriculture has taken her from Brooklyn to South Korea, China, Bangladesh, India, Poland, France, Italy, Mali, Kenya, South Africa, Zimbabwe, Botswana, Brazil, Mexico, Canada, and beyond.

Elizabeth Neilson: Elizabeth A. "Betty" Neilson, EDD (October 13, 1911 – October 4, 2001) was a prominent figure in the field of health education and a leader in promoting the wellness and holistic health perspectives in public health.

Question: Who is the Lithuarnian-American "holistic health" practitioner, food advocate and promoter of rejuvelac?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual."
    },
    "nationalities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of nationalities associated with the person."
    },
    "professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions or roles held by the person."
    },
    "advocacies": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of causes or practices the person advocated for."
    },
    "promoted_items": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of specific items or concepts promoted by the person."
    }
  },
  "required": [
    "person_name",
    "nationalities",
    "professions",
    "advocacies",
    "promoted_items"
  ],
  "additionalProperties": false
}
