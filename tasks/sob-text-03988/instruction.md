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
Weightlifting at the 2014 Commonwealth Games: Weightlifting competitions at the 2014 Commonwealth Games in Glasgow, Scotland were held between 24 July and 2 August at the Scottish Exhibition and Conference Centre.  Included with the weightlifting event were four powerlifting events for disabled athletes.

Judo at the 2014 Commonwealth Games: Judo competitions at the 2014 Commonwealth Games in Glasgow, Scotland were held from 24 July to 26 July at the Scottish Exhibition and Conference Centre.  Judo returned to the program after last being held at the 2002 Commonwealth Games.

Alien War: Alien War was a "total reality" experience in the United Kingdom that originally opened at the Arches in Glasgow in April 1992 themed around the Alien series of films.  Created by John Gorman and Gary Gillies, the attraction had a short run as a mobile event at various exhibition centres in the UK (including the Bournemouth International Centre and the Aberdeen Exhibition and Conference Centre).  On 15 October 1993 it opened in the basement of the Trocadero centre in London.  The permanent attraction in London closed after a flood in August 1996 and was never reopened.  It made a short return between December 1999 and January 2000 in the Scottish Exhibition and Conference Centre in Glasgow in a modified form.

Judo at the 2014 Commonwealth Games – Men's 60 kg: The men's 60 kg Judo competitions at the 2014 Commonwealth Games in Glasgow, Scotland was held on 24 July at the Scottish Exhibition and Conference Centre.  Judo returned to the program, after last being competed back in 2002.

Gymnastics at the 2014 Commonwealth Games: Gymnastics competitions at the 2014 Commonwealth Games in Glasgow, Scotland, was held from 24 July to 1 August at the SSE Hydro arena at the Scottish Exhibition and Conference Centre.

Judo at the 2014 Commonwealth Games – Men's 66 kg: The men's 66 kg Judo competitions at the 2014 Commonwealth Games in Glasgow, Scotland was held on 24 July at the Scottish Exhibition and Conference Centre.  Judo returned to the program, after last being competed back in 2002.

Kelvin Hall: The Kelvin Hall in Argyle Street Glasgow, Scotland, is one of the largest exhibition centres in Britain and now a mixed-use arts and sports venue that opened as an exhibition venue in 1927.  It has also been used as a concert hall, home to the Kelvin Hall International Sports Arena to 2014, and from 1987 to 2010, Glasgow's Museum of Transport.  As part of the economic redevelopment of Greater Glasgow promoted by the Scottish Development Agency and local authorities to enhance the city's tourist infrastructure and to attract further national and international conferences the Scottish Exhibition and Conference Centre was designed as the Hall's successor for exhibitions and entertainments, built and opened on the nearby Queen's Dock in 1985 with an exhibition area equal in size to the Kelvin Hall but with the benefit of extensive car parks and land for other complementary buildings.

Jina Devi Chongtham: Jina Devi Chongtham (born 3 February 1987) is an Indian judoka.  She is competing in the half-heavyweight (78 kg) class at the 2014 Commonwealth Games in Glasgow.

Vera Moskalyuk: Vera Sergeyevna Moskalyuk (Russian: Вера Сергеевна Москалюк; born 10 November 1981 in Zhytomyr, Ukraine) is a Ukrainian-born Russian judoka.  She competed in three consecutive Summer Olympics.  In 2004 in Athens in the -78 kg event she was eliminated in her first match by Liu Xia.  In Beijing in 2008 she competed again at -78 kg and lost her first match to Esther San Miguel.  Finally in London in 2012, still in the -78 kg event she was defeated by Kayla Harrison.

Rajwinder Kaur (judoka): Rajwinder Kaur (born 2 April 1984) is an Indian judoka.  She won the bronze medal in the +78 kg weight class at the 2014 Commonwealth Games in Glasgow, Scotland.

Question: Jina Devi Chongtham, is an Indian judoka, she is competing in the half-heavyweight (78 kg) class at which competitions in Glasgow, Scotland were held from 24 July to 26 July at the Scottish Exhibition and Conference Centre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "competition_name": {
      "type": "string",
      "description": "The name of the competition."
    },
    "event_details": {
      "type": "object",
      "properties": {
        "venue": {
          "type": "string",
          "description": "The venue where the competition was held."
        },
        "city": {
          "type": "string",
          "description": "The city where the competition was held."
        },
        "country": {
          "type": "string",
          "description": "The country where the competition was held."
        },
        "start_date": {
          "type": "string",
          "format": "date",
          "description": "The start date of the competition."
        },
        "end_date": {
          "type": "string",
          "format": "date",
          "description": "The end date of the competition."
        }
      },
      "required": [
        "venue",
        "city",
        "country",
        "start_date",
        "end_date"
      ],
      "additionalProperties": false
    },
    "athlete_details": {
      "type": "object",
      "properties": {
        "athlete_name": {
          "type": "string",
          "description": "The name of the athlete."
        },
        "sport": {
          "type": "string",
          "description": "The sport the athlete competes in."
        },
        "weight_class_kg": {
          "type": "integer",
          "description": "The weight class of the athlete in kilograms."
        }
      },
      "required": [
        "athlete_name",
        "sport",
        "weight_class_kg"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "competition_name",
    "event_details",
    "athlete_details"
  ],
  "additionalProperties": false
}
