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
Brandeis International Business School: Brandeis International Business School (IBS) is part of Brandeis University, located in Waltham, Massachusetts.  Brandeis IBS offers graduate degree programs in business, finance and economics, with over 3,000 alumni in over 100 countries.  Academics at Brandeis IBS focus on themes of international business and global economics, supplemented by over 70 faculty members, all of whom have research or corporate experience.  Bruce R. Magid served as dean of the school from 2007 - 2016.  Founding dean Peter Petri currently serves as the interim dean of the school.

London Business School: The London Business School (LBS) is an international business school and a constituent college of the federal University of London.  LBS was founded in 1964 and awards post-graduate degrees (master's degrees in management and finance, MBA, PhD and EMBA).  It is widely considered to be one of the leading business schools in Europe and is one of the few schools in the world to have the triple crown accreditation (AACSB, EQUIS, AMBA).

INCAE Business School: INCAE Business School is an international business school located at the Francisco de Sola campus in Nicaragua and the Walter Kissling Gam campus in Costa Rica.  The "Financial Times" has ranked INCAE as a top global MBA program and "The Wall Street Journal" has ranked INCAE Business School as one of the top 10 international business schools in the world.

ESB Business School: The ESB Business School (formerly "ESB Reutlingen") is Reutlingen University's business school founded in 1979 and based in Baden-Württemberg, Germany.  Since 2008, the school is responsible for all business related degree programs of the university.  In addition to the former ESB programs, it also includes the former School of International Business (SIB) and Production Management (PM).  The school offers 20 undergraduate and graduate programs as well as double degree programs in cooperation with numerous other business schools from around the world.  The ESB Business School ranks among the top business schools in Germany.

IPMI International business school: IPMI International Business School (formerly Indonesia Institute for Management Development) is a business school located in Jl.  Rawajati Timur I/1, Kalibata, South of Jakarta, Indonesia.  It offers both bachelor's and master's degrees in business administration, along with some other business programs available, all delivered in English.  Starting from 2012, IPMI International Business School is also focusing on business research in order to improve business in Indonesia.

The Reading School of International Business: The Reading School of International Business is widely understood in the field of international business (IB), management and economics to embody a stream of conceptual, and theoretically-driven empirical research, and consists of a group of economists and international business scholars who share a common approach to analyzing multinational enterprise and foreign direct investment.  Some are based in the Department of Economics and in Henley Business School at the University of Reading, England, but membership is international.  The Reading School builds upon the pathbreaking theoretical work of Peter Buckley and Mark Casson on internalization theory.  This was complemented by simultaneous work by John Dunning as he developed the eclectic paradigm of international business as an envelope explanation containing three principal drivers of foreign direct investment, comprising ownership (O); location (L); and internalization (I).  The Reading School approach continues through the work of its academic disciples around the world, as well as through The John Dunning Centre at Henley Business School, University of Reading, under the directorship of Rajneesh Narula.

Munich Business School: Munich Business School (MBS) is a private international business school located in Munich (Bavaria, Germany).  Munich Business School confers degrees exclusively in business administration.  It offers one undergraduate Bachelor program, 4 graduate Programs (Masters and MBA), a terminal DBA degree in cooperation with Sheffield Hallam University as well as double degree programs in cooperation with numerous other business schools from around the world.  Munich Business School ranks among the top private Business Schools in Germany and in the top 25 performers group regarding internationality and student mobility.

Paris School of International Affairs: The Paris School of International Affairs (PSIA) is a graduate school of Sciences Po (also referred to as the "Institut d'études politiques de Paris") based in Paris, France, and it is generally considered to be one of the top rated and most prestigious graduate schools for international relations in the world.  Located in the Saint-Germain-des-Prés neighborhood in the 7th arrondissement of Paris, the school has an international student population of 70%, with 1200 students coming from nearly 100 countries.

HEC Paris: HEC Paris ("Hautes études commerciales de Paris" ) is an international business school located in Paris, France.  It is widely considered to be one of the most prestigious and selective graduate schools in the world.  It was consistently ranked 1st in Europe from 2006 to 2013, and 2nd in Europe from 2014 to 2016 in the "Financial Times" ranking of European Business Schools .  In 2016, "Forbes" ranked HEC Paris 3rd globally for its International Two-Year MBA programme .  In "The Economist" 2016 Full-Time MBA rankings, HEC Paris's MBA programme was ranked 9th worldwide .  The admission to HEC Paris is extremely competitive with an acceptance rate of 8% .

Bernard Ramanantsoa: Bernard Ramanantsoa (born 26 November 1948) was the Dean of HEC Paris between 1996 and 2015.

Question: Who was the dean of an international business school located in Paris, France that is widely considered to be one of the most prestigious and selective graduate schools in the world, between 1996 and 2015?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "dean_name": {
      "type": "string",
      "description": "The name of the dean."
    },
    "school_name": {
      "type": "string",
      "description": "The name of the international business school."
    },
    "school_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string"
        },
        "country": {
          "type": "string"
        }
      },
      "required": [
        "city",
        "country"
      ],
      "additionalProperties": false
    },
    "dean_tenure_start_year": {
      "type": "integer",
      "description": "The start year of the dean's tenure."
    },
    "dean_tenure_end_year": {
      "type": "integer",
      "description": "The end year of the dean's tenure."
    },
    "school_prestige_description": {
      "type": "string",
      "description": "A description of the school's prestige as mentioned in the context."
    }
  },
  "required": [
    "dean_name",
    "school_name",
    "school_location",
    "dean_tenure_start_year",
    "dean_tenure_end_year",
    "school_prestige_description"
  ],
  "additionalProperties": false
}
