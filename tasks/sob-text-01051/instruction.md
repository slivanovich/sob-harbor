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
Jonathon Lyons: Jonathon Edward Lyons (born 1951 in Leeds) is a British-Canadian businessman and is the owner and chairman of JE London Properties.  He is the youngest son of the financier Isidore Jack Lyons, (SirJack Lyons CBE)a former director of the UDS Group.  Jonathon Lyons made his fortune in the property and venture capital sectors as well as retail,He had large investments in the middle east Overseas Director (Ronson PLC and Remington)in the distribution licensing sector.Appointed director of REGENTFLAG LIMITED in February 1990,JLC (LONDON) LTD, appointed director feb 1990 also director SOUTH BANK PENSION FUND TRUSTEES LIMITED on the same day of the same month( 28 feb 1990.  Appointed director of J E LONDON PROPERTIES LIMITED 31 dec 1991. aPPOINTED DIRECTOR OF BELLCROWN ESTATES LTD(DISSOLVED)5 February 1998.  Appointed director of 37 COLVILLE TERRACE MANAGEMENT COMPANY LIMITED Switzerland.  A large proportion of the Lyons family holdings stretch across many freeholds within and around the Notting Hill and Kensington areas as well as large property holdings in the United States.

Goodbye Mr. Black: Goodbye Mr. Black () is a 2016 South Korean television series based on the manhwa of the same title what produced by the novel The Count of Monte Cristo motif, written by and published in 1983.  It airs on MBC on Wednesdays and Thursdays at 21:55 (KST) from March 16, 2016 to May 19, 2016 for 20 episodes.

Sunmin: Sunmin (Hangul: 선민, "Katakana": ソンミン, born August 4, 1987) is a South Korean singer who speaks and sings in Korean, Japanese, and English.  She debuted in 2006, with the single "Keep Holding You," a collaboration with the Japanese R&B singer Toshinobu Kubota.  Her career was initially focused on the Japanese market, but her work became focused in South Korea from 2009 to 2010.  She also contributed to original soundtracks of South Korean television series "Master of Study" and "Gloria (2010 TV series)".  In 2010 to 2011, she was in the main South Korean musical production of "Jekyll & Hyde" as Lucy.  In 2012 to 2013, she reprised her role as Lucy in the South Korean national tour.  In spring 2013, Sunmin played Josephine in the South Korean production of "Arsène Lupin", the musical.

Kang So-ra: Kang So-ra (born February 18, 1990) is a South Korean actress.

The Master of Revenge: The Master of Revenge () is a 2016 South Korean television series starring Chun Jung-myung, Jo Jae-hyun, Jeong Yoo-mi, Lee Sang-yeob and Gong Seung-yeon.  It aired on KBS2 from April 27, 2016 to June 30, 2016 on Wednesdays and Thursdays at 21:55 for 20 episodes.

Chae Shi-ra: Chae Shi-ra (born June 25, 1968) is a South Korean actress born in Seoul.  Since 1990, Chae has firmly established her acting career with "Eyes of Dawn" in the 1990s, she was referred to as a representative actress of the period along with Kim Hee-ae and Ha Hee-ra.

My Lawyer, Mr. Jo: My Lawyer, Mr. Jo (; also known as "Neighborhood Lawyer Jo Deul-ho") is a 2016 South Korean television series starring Park Shin-yang, Kang So-ra, Ryu Soo-young, Park Sol-mi.  Based on the same-titled webtoon, it aired on KBS2.

Heo Jung-eun: Heo Jung-eun (; born September 1, 2007) is a South Korean actress.  She first drew public attention with her performances in hit dramas, "My Lawyer, Mr. Jo" (2016) and "Love in the Moonlight" (2016).  At age nine, she took on her first leading role in television as Geum-bi, a girl who suffers from childhood Niemann–Pick disease in" My Fair Lady" (2016).

The Gentlemen of Wolgyesu Tailor Shop: The Gentlemen of Wolgyesu Tailor Shop () is a 2016 South Korean television series starring Lee Dong-gun, Jo Yoon-hee, Shin Goo, Cha In-pyo, Choi Won-young, and Hyun Woo.  The series aired on KBS2 every Saturday and Sunday from 7:55 p.m. to 9:15 p.m. (KST).  The series served as Kim Young-ae's final work, as she died almost 2 months after the final episode.

Yoo Da-in: Yoo Da-in (born Ma Young-seon on February 9, 1984) is a South Korean actress.  She is best known for her nuanced performance in the critically acclaimed indie film "Re-encounter", her first leading role.  In 2016, she played a supporting role in South Korean television series "Doctor Crush".

Question: Which South Korean actress born in Feb 1990 appears on the 2016 South Korean television series "My Lawyer, Mr. Jo"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the South Korean actress."
    },
    "birth_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The birth year of the actress."
        },
        "month": {
          "type": "string",
          "description": "The birth month of the actress."
        }
      },
      "required": [
        "year",
        "month"
      ],
      "additionalProperties": false
    },
    "tv_series_appearance": {
      "type": "object",
      "properties": {
        "series_title": {
          "type": "string",
          "description": "The title of the television series the actress appeared in."
        },
        "series_year": {
          "type": "integer",
          "description": "The year the television series aired."
        }
      },
      "required": [
        "series_title",
        "series_year"
      ],
      "additionalProperties": false
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actress."
    }
  },
  "required": [
    "actress_name",
    "birth_details",
    "tv_series_appearance",
    "nationality"
  ],
  "additionalProperties": false
}
