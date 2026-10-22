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
The Very Best of Cilla Black: The Very Best of Cilla Black is an original, career-spanning compilation album by English singer Cilla Black, released in October 2013 by Parlophone / Warner Music Group UK to mark her golden anniversary in show business.  The album reached No. 37 in 2013 on the UK Albums Chart, which was Black's first Top 40 hit in thirty years.  In September 2014, after the transmission of ITV biopic "Cilla" starring Sheridan Smith the album re-entered the UK Albums Chart and peaked at No. 26.  The album was to make its ultimate peak at No. 1 after Black's death in August 2015, becoming her first number one album.  It also reached No. 1 in New Zealand on 21 August 2015 and stayed there for 5 consecutive weeks, making it the first album to achieve this since Sole Mio's eponymous album in March 2014.

Ioane Ioane: Ioane 'John' Ioane (born 1962) is a New Zealand artist of Samoan descent.  His work is informed by his Samoan heritage and includes performance, film, painting, installation and sculpture.  In conversation about his work "Fale Sā" with art historian Caroline Vercoe, Ioane states, "Sacred places are not necessarily a church, but it's a place where one likes to be in, a place of affirmation."  Curator Ron Brownson writes, "Ioane's attitude to sculptural process is cosmological – his carvings bind present reality with a representation of the past."

Tha Feelstyle: Tha Feelstyle is the stage name of award-winning hip hop artist Kas Futialo, a New Zealander of Samoan descent.  His first album was "Break It To Pieces" in 2004.  Tha Feelstyle was born in Samoa and moved to New Zealand in the 1980s.  He raps in English as well as the Samoan language.

Sole Mio: Sole Mio (stylised as SOLΞ MIO) is a New Zealand musical trio consisting of brothers Pene Pati and Amitai Pati and their cousin Moses Mackay.  Of Samoan descent and classically trained, the Pati brothers are operatic tenors and Mackay is a baritone.

Fosi Pala'amo: Fosi Pala'amo (born 23 August 1976) is a New Zealand professional rugby player of Samoan descent.  Internationally, he plays for Samoa.  He was born in Murupara, New Zealand to Samoan parents.  He was formerly a player for the Irish team Leinster Rugby, but now plays for the Irish side Monkstown RFC.

Lily Laita: Lily Aitui Laita (born 1969) is an artist and art educator in New Zealand.  Laita is of mixed Pākehā and Māori ancestry (Ngāti Raukawa), as well as of Samoan descent.  Laita is known for using Māori, English and Samoan texts in her paintings.

Mose Masoe: Mose Masoe (born 17 May 1989) is a New Zealand professional rugby league footballer of Samoan descent who currently plays for Hull Kingston Rovers in the Kingstone Press Championship.  A Samoan national representative prop, he previously played for the Sydney Roosters, Penrith Panthers and the St. George Illawarra Dragons and for St. Helens in the Super League, with whom he won the 2014 Super League Grand Final.

Ladi6: Ladi6 (born Karoline Tamati, 7 November 1982 in Christchurch, New Zealand,) is a recording artist of Samoan descent.  She spent six months living in Berlin and touring Europe in both 2010 and 2011.  Her debut album "Time Is Not Much" debuted at number 4 on the New Zealand Top 40 Album chart.  and her second album "The Liberation Of..." debuted at number 6 and was certified gold.  Her single Like Water was certified platinum in June 2011.  She has won many awards, including Best Female Solo Artist and Best Urban Hip Hop Album at the 2011 New Zealand Music Awards and Best Urban/Hip Hop Album at the 2009 New Zealand Music Awards.  The current line-up of the wider Ladi6 group is Ladi6, her partner Parks (a.k.a. Brent Park) and Julien Dyne.  Ladi6 has been called "New Zealand's answer to Erykah Badu".

Polarkreis 18: Polarkreis 18 was a German pop band from Dresden, Saxony.  The bandmembers met at school, where they formed the Jack of all Trades ensemble in 1998.  In 2004, they renamed their band "Polarkreis 18".  Its musical style can be described as pop, synthpop and indietronic.  Their albums include "Polarkreis 18" and more recently "The Colour Of Snow".  Their single "Allein Allein" (Alone Alone) reached the number one position on the German Media Control Top100 Singles chart from 31 October 2008 to 4 December 2008 for 5 consecutive weeks and another 8 weeks on position number 2.  It is one of the most successful singles in that country of all time.  It has also been in the top ten of several other countries throughout Europe.  It also made the number 1 position for 5 consecutive weeks in Denmark with a remake version of the Danish band Nephew.

Lani Tupu: Lani Tupu (born 4 November 1955 in Auckland, New Zealand), billed variously as Larney Tupu, John Tupu and Lani John Tupu, is a New Zealand-born classically trained actor of Samoan descent.  He was educated at Rongotai College and Wellington Teacher's Training College.  He was awarded a Queen Elizabeth II Arts Council Bursary in 1977 to enter New Zealand Drama School, where he graduated in 1978.  Lani left New Zealand for Australia in 1985 to "branch out across the big pond."

Question: What brothers of Samoan descent recorded an album that reached No. 1 in New Zealand and stayed there for 5 consecutive weeks?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musical_group": {
      "type": "string",
      "description": "The name of the musical group."
    },
    "members": {
      "type": "array",
      "description": "List of members in the group who are brothers.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the brother."
          },
          "role": {
            "type": "string",
            "description": "The role of the member in the group (e.g., operatic tenor, baritone)."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "descent": {
      "type": "string",
      "description": "The ethnic descent of the artists."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_name": {
          "type": "string",
          "description": "The name of the album."
        },
        "chart_peak_position": {
          "type": "integer",
          "description": "The highest position the album reached on the chart."
        },
        "chart_country": {
          "type": "string",
          "description": "The country where the album charted."
        },
        "weeks_at_peak": {
          "type": "integer",
          "description": "The number of consecutive weeks the album stayed at its peak position."
        },
        "chart_year": {
          "type": "integer",
          "description": "The year the album achieved its chart success."
        }
      },
      "required": [
        "album_name",
        "chart_peak_position",
        "chart_country",
        "weeks_at_peak",
        "chart_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "musical_group",
    "members",
    "descent",
    "album_details"
  ],
  "additionalProperties": false
}
