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
New York Minute (film): New York Minute is a 2004 American teen comedy film starring Mary-Kate Olsen, Ashley Olsen and Eugene Levy.  It was directed by Dennie Gordon and released on May 7, 2004.  In the film Mary-Kate and Ashley play twins with opposing personalities who have a series of misadventures around New York City.  "New York Minute" reunited Mary-Kate and Ashley with their "Full House" co-star, Bob Saget.  It was the Olsen twins' first theatrical film release since 1995's "It Takes Two".  It was also the last film featured by Olsen twins, and the last film released by Dualstar Entertainment before it went into dormancy.

Mary-Kate Olsen: Mary-Kate Olsen (born June 13, 1986) is an American fashion designer, producer, author, businesswoman, equestrian, and former actress.  She co-founded luxury fashion brands The Row, Elizabeth and James, and the more affordable lines Olsenboye and StyleMint alongside her fraternal twin sister Ashley Olsen.  Olsen pursued acting independently as an adult until 2012.  She is an older sister of actress Elizabeth Olsen.

EMEL Fashion: EMEL Fashion is an American fashion design house that is based in Los Angeles, California.  The company's name comes from the letters "M" and "L", which stand for "Michelle Liu", the Taiwanese born chief designer and co-founder of EMEL Fashion.  According to its Facebook fan page, EMEL Fashion specializes in contemporary lady's fashion apparels and distinguishes itself from other fashion houses by using proprietary economic models designed by Ken Wu, the managing director and co-founder, to aid its style and design research.

The Row (fashion label): The Row is an American luxury fashion design house founded in 2006 by Ashley Olsen and Mary-Kate Olsen.  The name was inspired by Savile Row in London.  Part of The Row's mission is to support high-end fashion manufacturing in the United States.

Kate Spade New York: Kate Spade New York is an American fashion design house founded in January 1993 by Kate Spade and Andy Spade.  Jack Spade is the brand's line for men.  Kate Spade New York competes with Michael Kors.  The company was recently purchased by, and is now part of, Coach.

Colombo Fashion Week: Colombo Fashion Week was conceived in 2003, as a project that was focused on uplifting Sri Lanka's fashion design industry.  Today it is firmly established as the backbone of Sri Lanka's fashion design industry and in its journey of over a decade it has taken Sri Lanka's fashion design industry from strength to strength.  CFW as its popularly known is probably one of 3 fashion weeks in Asia that is over ten years.  It is developmental in its nature, which covers every aspect of a fashion design industry from grooming young designer at college level, to guiding senior and established designers through commercial opportunities.

JJ Valaya: JJ Valaya (born 8 October 1967) is a noted Indian fashion designer and couturier from New Delhi, India.  He founded the House of Valaya, a luxury fashion and lifestyle house in 1992, along with his brother TJ Singh.  A founding member of Fashion Design Council of India (FDCI) and the first global brand ambassador of Crystal giant Swarovski, he has been designing for men and women, and has bridal and evening collections in addition to day-wear and ready-to-wear for over 20 years.  As a fine art photographer, he released his first book, "Decoded Paradox" in 2011, in the same year as he also closed the day one of the Lakme Fashion Week (LFW) winter/festive 2011, debuting a fashion collection inspired by photography.

Mary-Kate and Ashley Olsen: Mary-Kate Olsen and Ashley Olsen (born June 13, 1986), also known as the Olsen twins collectively, are American fashion designers and former child actresses.  The fraternal twins made their acting debut as infants playing Michelle Tanner on the television series "Full House".  At the age of six, Mary-Kate and Ashley Olsen began starring together in TV, film, and video projects, which continued to their teenage years.  Through their company Dualstar, the Olsens joined the ranks of the wealthiest women in the entertainment industry at a young age.

Ashley Olsen: Ashley Fuller Olsen (born June 13, 1986) is an American fashion designer, producer, author, businesswoman, and former actress.  She co-founded luxury fashion brands The Row, Elizabeth and James, and the more affordable lines Olsenboye and StyleMint with her fraternal twin sister Mary-Kate Olsen.  She is the older sister of actress Elizabeth Olsen.

Iceberg (fashion house): Iceberg is an Italian luxury fashion design house.  Founded in 1974 by Silvano Gerani and Giuliana Marchini, the house produces women’s and men's' 'prêt-a-porter", accessories, fragrances and childrenswear.  It is part of the Gilmar Group, founded in 1962.

Question: The Row is an American luxury fashion design house founded in 2006 by Mary-Kate Olsen, and who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fashion_house_name": {
      "type": "string",
      "description": "The name of the fashion design house."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the fashion house was founded."
    },
    "founders": {
      "type": "array",
      "description": "A list of individuals who founded the fashion house.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of a founder."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the fashion house is based."
    },
    "is_luxury_brand": {
      "type": "boolean",
      "description": "Indicates if the fashion house is a luxury brand."
    }
  },
  "required": [
    "fashion_house_name",
    "founding_year",
    "founders",
    "country_of_origin",
    "is_luxury_brand"
  ],
  "additionalProperties": false
}
