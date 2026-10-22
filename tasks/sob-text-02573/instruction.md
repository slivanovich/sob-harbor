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
Pearl School of Business: Pearl School of Business (PSB) is a Business School in India, founded by House of Pearl in 2006.  The group also runs Fashion Institute, Pearl Academy of Fashion and Indian Retail School.  It offers graduate and post-graduate programmes including two year MBA, BBA, one year Executive MBA and DBA.  PSB is located in Millennium City, Gurgaon, one of the hubs in India for IT and ITES companies.

Iris Maity: After her graduation in science, she earned an MBA degree in marketing.  She is a trained dancer, and can also sing and paint.  Her father, Bhaskar Maity, is a former football player, who represented India in the Asian Games, 1979.  Her mother is a homemaker, and she also has a younger brother.  Iris was crowned "Get Gorgeous" 2008.  "Get Gorgeous" is Channel V's launch pad for aspiring models across India.  As winner of Channel [V] "Get Gorgeous" 5, Iris won million () contract with Channel V and ICE Model Management.  She also won Miss India Tourism Metropolitan in 2007.  She was adjudged with the "I AM Photogenic" title at the I AM She 2010, the first Miss India Universe pageant, which was held on 28th May 2010 in Mumbai.  She is also trained in Martial Arts.

Édouard Carmignac: Édouard Carmignac (born 5 September 1947 in Paris) is a French investment banker and fund manager.  He currently is the head of Carmignac Gestion, an investment firm that bears his name.  Carmignac graduated in economics from the University of Paris and received an M.B.A. from Columbia Business School.  Prior to Carmignac Gestion, he had spells with Blyth, Eastman, Dillon & Co. in New York City and BNP Paribas in Paris.  In 1984 he joined stockbrokers Hamant & Cie and subsequently played an instrumental role in the creation of the firm's fund management subsidiary, Pyramide Gestion.

IESE Business School: IESE Business School is the graduate business school of the University of Navarra.  IESE offers Master of Business Administration (MBA), Executive MBA and Executive Education programs that have often ranked among the top 10 in the world.  IESE has campuses in Barcelona, Madrid, and New York City and teaching facilities in Munich and Sao Paulo.  IESE is an initiative of Opus Dei, a personal prelature of the Catholic Church.

Édouard Du Puy: Édouard Du Puy was born in Corcelles-Cormondrèche, Canton of Neuchâtel, Switzerland, around the year 1770, although sources differ on the exact year.  From the age of four, he was raised by his uncle, a city musician in Geneva, whose last name Edouard later took.  Seeing that his nephew had talent, the uncle made sure that Edouard became a musician of education.

Columbia Business School: Columbia Business School (CBS) is the business school of Columbia University in Manhattan, New York City.  It is one of six Ivy League business schools, and is among the most selective of top business schools.  The school belongs to the M7 group of elite MBA programs which recognize each other as peers, consisting of Chicago Booth, Columbia, Harvard, Kellogg, MIT Sloan, Stanford, and Wharton.

Circle of Friends of the Medallion: Circle of Friends of the Medallion was formed by Charles DeKay, Robert Hewitt, Jr., and the French-American trio of Jules Edouard Roiné with brothers Felix and Henri Weil, all living in New York City.  De Kay, "a newspaperman and art lover" provided the contacts to form the Circle of Friends of the Medallion, often referred to as the Circle of Friends, while Hewitt, "a Manhattan real estate investor" provided the funds for its development.  Jules Edouard Roiné and Felix Weil ran the Roiné, Weil and Company (1908-1916) which they collaborated with Henri.  Upon Roiné's passing in 1916, Felix and Henri Weil operated the Medallic Art Company of New York.  The three men, via both companies, made the 1st, 2nd and 12th medals in the series.  Joseph K. Davison & Sons of Philadelphia struck the other medals.

Hurricane Edouard (1996): Hurricane Edouard was the strongest hurricane in the 1996 Atlantic hurricane season, reaching winds of 145 mph (230 km/h) on its path.  Edouard remained a major hurricane for eight days, an unusually long amount of time.  A Cape Verde-type hurricane, the storm formed near the coast of Africa in the middle of August.  It moved westward then curved northward, and persisted until early September when it became extratropical to the southeast of New England.  Edouard was originally forecast to strike the northeast United States, but it produced hurricane-force gusts to portions of southeastern Massachusetts while remaining offshore.  The winds caused minor damage totaling $20 million.  In addition, the hurricane generated strong waves and rip currents to coastlines, killing two people in Ocean City, Md and causing numerous injuries.

R. A. Podar Institute of Management: R. A. Podar Institute of Management, Faculty of Management Studies is a provider of management education in Jaipur city, in Rajasthan state, India.  It was set up in 1974 as a constituent unit of the University of Rajasthan .  The institute offers courses such as MBA( SM), MBA(Executive).  The institute campus at J.L.N. Road is spread over an area of 20,000 sq meters.

FMS Baroda: M S Patel Institute of Management Studies, known as FMS-Baroda, was established in 1984 in the city of Vadodara.  It is run by the Maharaja Sayajirao University of Baroda.  The courses are approved by All India Council for Technical Education.  During 1995, it increased its intake from 30 to 40 for 2-year full-time (regular) MBA, and in 1997 introduced a 3-Year MBA Evening Programme.  The institute is consistently rated among the top five management institutes run by University in India.  The Business School has been consistently rated as 'A' grade by Business India magazine in 2007 and 2008.

Question: What city did Edouard get his MBA in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person who obtained the degree."
    },
    "degree_type": {
      "type": "string",
      "description": "The type of degree obtained, e.g., MBA."
    },
    "institution_name": {
      "type": "string",
      "description": "The name of the educational institution where the degree was obtained."
    },
    "city_of_institution": {
      "type": "string",
      "description": "The city where the educational institution is located."
    }
  },
  "required": [
    "person_name",
    "degree_type",
    "institution_name",
    "city_of_institution"
  ],
  "additionalProperties": false
}
