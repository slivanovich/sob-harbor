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
Paul Jr. Designs: Paul Jr.  Designs (PJD) is a lifestyle brand motorcycle customizer and clothing vendor based in Rock Tavern, New York, USA.  Paul Teutul Jr. founded the design firm in 2009 after waiting out a one-year non-compete clause with his former company, Orange County Choppers (OCC).

City &amp; State: City & State is a political journalism organization based in New York City.  The company publishes a weekly magazine covering politics and government in New York City and New York State that is distributed to New York State legislators, county executives, municipalities, the New York Congressional delegation, New York City Council members and others leaders in New York business and government.  After years of publishing a twice-monthly print edition, "City & State" has announced plans to switch to a weekly in January 2016.  "City & State" also publishes on their website and sends out a free First Read daily email.  In May 2016 the company also launched a monthly magazine based in Philadelphia and a website.

Katherine Oliver: Katherine Oliver is an American media and entertainment executive based in New York City.  Oliver is currently a Principal at Bloomberg Associates, a philanthropic consultancy firm founded by Michael Bloomberg to provide advice and long-term solutions to cities worldwide.  On August 1, 2002, she was appointed by New York City Mayor Michael Bloomberg as the Commissioner of The New York City Mayor's Office of Film, Theatre and Broadcasting, which facilitates all aspects of film, television and commercial production in New York City, coordinating on-location filming, liaising with the community and promoting the City as an entertainment capital.  Oliver was the main liaison between the Mayor's Office and Hollywood and aimed "to make filmmakers and production companies happy to return to New York."  In 2013, Oliver and Mayor Bloomberg were featured on the cover of Variety and were credited for their role in "revitalizing the city's entertainment sector."  An economic impact study released by the Boston Consulting Group in 2012 found that New York City's entertainment industry during Oliver's tenure as film commissioner had grown to account for a $7.1 billion annual direct spend in New York City, an increase of $2 billion since 2002, and that the local industry created 30,000 jobs in New York City since 2004, growing to employ 130,000 people.  AM New York noted that: "New York's film and TV industry is stronger than it has ever been, pumping $7.1 billion into the local economy in 2011 and bringing in some $60 billion over the last decade."  After Bloomberg announced that former president and co-founder of NYC Media Group Arick Wierson was returning to the private sector, Bloomberg named Oliver as the incoming president of NYC Media and general manager of NYCTV.  In July 2010, Oliver became the commissioner of the Mayor's Office of Media and Entertainment, the city agency that includes the Mayor's Office of Film, Theatre and Broadcasting, NYC Media, and NYC Digital.

School of American Ballet: The School of American Ballet (SAB) is an American classical ballet school and is the associate school of the New York City Ballet, a ballet company based at the Lincoln Center for the Performing Arts in New York City.  The school trains students from the age of six, with professional vocational ballet training for students aged 11–18.  Graduates of the school achieve employment with leading ballet companies worldwide, most notably in the United States with New York City Ballet, American Ballet Theatre, Boston Ballet, and San Francisco Ballet.

Center for Contemporary Opera: The Center for Contemporary Opera (CCO) is a professional opera company based in New York City, and a member of OPERA America.  The company focuses on producing and developing new opera and music theater works and reviving rarely seen American operas written after the second World War.  The Center for Contemporary Opera has staged the premieres of many works written during the latter half of the twentieth century.  Works are performed at all stages of development from readings to workshops to full productions on the professional stage.  In line with its mission to promote an interest in new operatic and music-theater culture among the American public, the company presents panel discussions and colloquia, and publishes a bi-annual newsletter "Opera Today".  Since 2004, the company has been a regular participant in the New York City Opera's annual festival, "Vox: Showcasing American Composers".

Orange County Choppers: Orange County Choppers (OCC) is a motorcycle manufacturer and lifestyle brand company based in the town of Newburgh, located in Orange County, New York, that was founded in 1999 by Paul Teutul Sr., and Paul Teutul Jr. The company was featured on "American Chopper", a reality TV show that debuted in September 2002 on the Discovery Channel.  The series moved to Discovery Channel's sister channel TLC in 2007.  Following cancellation of the Discovery series, the company was also featured on "Orange County Choppers" on the CMT network in 2013.

Azeroth Choppers: Azeroth Choppers was a weekly web series by Blizzard Entertainment that ran from April 17 to June 5, 2014.  It featured Paul Teutul, Jr. ("American Chopper") and his company Paul Jr.  Designs building motorcycles based on Blizzard's long-running MMORPG "World of Warcraft".

The New York Enterprise Report: The New York Enterprise Report or "' NY Report"' is a media company based in New York City, New York.  The company is founded on the belief that all business owners should have access to the expertise that will help them grow their companies.  The business caters to entrepreneurs and executives who constantly seek better ways to operate and grow.  Through NY Report’s multi-media platforms, they provide their readers with access to knowledge from experts and inspiration from successful entrepreneurs.The publication mainly covers local small businesses, that are located within the Greater New York Area.  The magazine uses expert-written news articles, tips, advice and other helpful resources to help small business owners expand their company.  The New York Enterprise Report puts out a monthly publication as well as publishes daily articles and interviews on their website to help people grow their businesses.

Tom Gold Dance: Tom Gold Dance (TGD) is a classical dance company based in New York City.  Founded in 2008 by former New York City Ballet soloist Tom Gold, Tom Gold Dance performs in New York City and throughout the world.

Central Park Media: Central Park Media was an American multimedia entertainment company based in New York City, New York, that was active in the distribution of East Asian cinema, television series, anime, manga and manhwa titles in North America prior to its bankruptcy in 2009.  It was headquartered in the 250 West 57th Street building in Midtown Manhattan, New York City.

Question: Azeroth Choppers featured the company based in what New York city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company featured in the series."
    },
    "featured_in_series": {
      "type": "string",
      "description": "The name of the web series where the company was featured."
    },
    "base_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the company is based."
        },
        "state": {
          "type": "string",
          "description": "The state where the company is based."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "featured_in_series",
    "base_location"
  ],
  "additionalProperties": false
}
