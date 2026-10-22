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
Mississippi Opera: The Mississippi Opera is an American opera company located in Jackson, Mississippi.  Founded in 1945, the company presents an annual season of opera consisting of two fully staged opera productions and smaller concerts and workshops open to the public.  The company's productions are performed at the Belhaven University Center for the Arts.  Composer William Grant Still and soprano Leontyne Price both have associations with the company.

Max Maretzek Italian Opera Company: The Max Maretzek Italian Opera Company (sometimes referred to as the Italian Opera Company, the Italian Grand Opera Company, or Academy of Music Opera Company) was a touring American opera company that performed throughout the United States from 1849-1878.  The first major opera company in Manhattan and one of the first important companies in the United States, it had a long association with the Academy of Music in New York City where it presented an annual season of opera from 1854 until the company's demise in 1878 There the company performed the United States premieres of "Rigoletto", "Il trovatore", and "La traviata" among other works.

Philadelphia La Scala Opera Company: The Philadelphia La Scala Opera Company (defunct) was an American opera company located in Philadelphia, Pennsylvania that was actively performing at the Academy of Music between 1925 and 1954.  In 1955 the company merged with the Philadelphia Civic Grand Opera Company to form the Philadelphia Grand Opera Company.

Philadelphia Lyric Opera Company: The Philadelphia Lyric Opera Company was an American opera company located in Philadelphia, Pennsylvania that was active between 1958 and 1974.  The company was led by a number of Artistic Directors during its history, beginning with Aurelio Fabiani.  Other notable Artistic Directors include Julius Rudel and Anton Guadagno (1966–1972).  The company produced between four and six of their own operas every year in addition to sponsoring numerous traveling productions from the New York City Opera.  In 1975 the company merged with the Philadelphia Grand Opera Company but retained its original name.  With the combined resources of both companies, the Philadelphia Lyric Opera Company began producing higher quality productions with name artists such as Luciano Pavarotti, Joan Sutherland, Roberta Peters, Montserrat Caballé, and others.  For the bicentennial year 1976, the company commissioned famed opera composer Gian Carlo Menotti to create a new opera.  The work, The Hero, premiered on June 1, 1976.  In 1980, the company artistically reorganized to form the Opera Company of Philadelphia.

Opera Company of Boston: The Opera Company of Boston was an American opera company located in Boston, Massachusetts, that was active from the late 1950s through the 1980s.  The company was founded by American conductor Sarah Caldwell in 1958 under the name Boston Opera Group.

American Opera Company: The American Opera Company was the name of four different opera companies active in the United States.  The first company was a short-lived opera company founded in New York City in February, 1886 that lasted only one season.  The second company was based out of Rochester, New York and was active from the mid-1920s up until 1930 when it went bankrupt not too long after the Wall Street Crash of 1929.  The third opera company was a short lived company located in Trenton, New Jersey that was active in 1937.  The fourth and last opera company was actively performing in Philadelphia from 1946 through 1950.

Philadelphia Civic Opera Company: The Philadelphia Civic Opera Company (PCOC) was an American opera company located in Philadelphia, Pennsylvania, that was actively performing between 1924 and 1930.  Founded by Philadelphia socialite Mrs. Henry M. Tracy, the company was established partially through funds provided by the city of Philadelphia and its then-mayor, W. Freeland Kendrick.  The company was led by Artistic Director Alexander Smallens.  Tracy served as the company's President and ran the business side of the organization while Smallens served as the company's primary conductor and made all of the artistic decisions.  W. Attmore Robinson was later brought in to help Smallens with some of the artistic direction.  The company performed between 10 and 15 operas every year during an annual season until it went bankrupt a year after the Wall Street Crash of 1929.

San Antonio Opera: The San Antonio Opera was an American opera company located in San Antonio, Texas that produced 16 seasons of opera before filing for bankruptcy and dissolving in 2012.  The company was founded as the Pocket Opera of San Antonio in 1997 by Mark Richter, and opened its first season in the fall of 1997 with Wolfgang Amadeus Mozart's "Der Schauspieldirektor" at the San Pedro Playhouse.  Initially the company's productions utilized local artists, but by the 1999-2000 season the company had begun employing internationally recognized artists.  It simultaneously rebranded itself as the Lyric Opera of San Antonio and began performing at the Lila Cockrell Theatre.  The opera company changed its name to the San Antonio Opera a few years later.  Notable artists to have performed with the company include Plácido Domingo, José Carreras, and Andrea Bocelli among others.

William Grant Still: William Grant Still (May 11, 1895 – December 3, 1978) was an American composer, who composed more than 150 works, including five symphonies and eight operas.

Philadelphia Grand Opera Company: The Philadelphia Grand Opera Company was the name of four different American opera companies active at the Academy of Music in Philadelphia, Pennsylvania during the twentieth century.  The last and best known of the four was founded in November 1954 with the merger of the Philadelphia Civic Grand Opera Company and the Philadelphia La Scala Opera Company.  That company in turn merged with the Philadelphia Lyric Opera Company in 1975 to form the Opera Company of Philadelphia.  Of the three earlier companies, only one lasted beyond one season; a company founded in 1926 which later became associated with the Curtis Institute of Music in 1929.  That company closed its doors in 1932 due to financial reasons during the Great Depression.

Question: What American composer who died in 1978 was associated with an American Opera Company located in Jackson, Mississippi?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the American composer."
        },
        "death_year": {
          "type": "integer",
          "description": "The year the composer died."
        }
      },
      "required": [
        "name",
        "death_year"
      ],
      "additionalProperties": false
    },
    "associated_opera_company": {
      "type": "object",
      "properties": {
        "company_name": {
          "type": "string",
          "description": "The name of the opera company the composer was associated with."
        },
        "location": {
          "type": "string",
          "description": "The city and state where the opera company is located."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the opera company was founded."
        }
      },
      "required": [
        "company_name",
        "location",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the composer who fits the criteria."
    }
  },
  "required": [
    "composer_details",
    "associated_opera_company",
    "final_answer"
  ],
  "additionalProperties": false
}
