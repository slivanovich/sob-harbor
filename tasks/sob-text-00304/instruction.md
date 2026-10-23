{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWhile the City Sleeps...: While the City Sleeps... is the 1986 studio album of George Benson on Warner Bros..  It features musicians like Paulinho da Costa, Preston Glass, Paul Jackson, Jr., Marcus Miller and Narada Michael Walden (as drummer and producer), alongside young talents of the time like Kenny G, Randy Jackson and Kashif.  It's part of the \"series\" of 1980s pop albums Benson recorded.  Though it doesn't have any instrumental tracks, Benson's guitar playing is somewhat in the headlight in songs like \"Love Is Here Tonight\", \"Teaser\" and \"Too Many Times\".  Beside being the most successful single, \"Kisses in the Moonlight\" is still frequently played by Benson at live performances and is present on many of his compilation albums (\"The Best of George Benson\", \"The George Benson Anthology\", \"The Essential Selection\", etc.) On the B-side of the \"Kisses in the Moonlight\" single – alongside \"Breezin'\" (Special Mix) on the 12\" version – is the instrumental song \"Open Your Eyes\" (George Benson/Ronnie Foster) (producer: Tommy LiPuma, engineer: Eric Calvi) which is not available elsewhere.\n\nClaudine Longet: Claudine Georgette Longet (born 29 January 1942) is a French singer, actress, dancer and recording artist who was popular during the 1960s and 1970s.\n\nBreezin' (song): \"Breezin'\" is an instrumental song composed by American singer and musician Bobby Womack.  It was originally recorded in December 1970 by the influential Hungarian jazz guitarist Gábor Szabó, in partnership with Womack himself.  The song was originally released in 1971 on the Szabó's album \"High Contrast\".  The song was released as a single in April 1971 in the United States and in 1972 in the Netherlands.  The single reached No. 43 on the R&B chart the same year.  \"Breezin'\" was produced by Tommy LiPuma.\n\nStuff (Stuff album): Stuff is the debut studio disc by the group Stuff, a team of renowned session musicians.  Released in 1976 on Warner Bros., it was produced by Herb Lovelle and jazz producer Tommy LiPuma.  The record earned RIAA gold status, and the group would go on to record two more studio discs, each of which also went gold.\n\nHolly &amp; Ivy: Holly & Ivy is a 1994 Christmas album and sixteenth overall by American singer Natalie Cole.  It was released on October 4, 1994, by Elektra; it is Cole's first album featuring Christmas music and serves as a follow-up to \"Take a Look\" (1993).  Cole co-produced the album with American music producer Tommy LiPuma, with whom she worked on \"Unforgettable... with Love\".  \"Holly & Ivy\" consists of twelve tracks, including eleven covers of Christmas standards and carols, and one original song written by Gerry Goffin and Michael Masser.  Cole promoted the album as \"non-traditional\" in interviews and performances.\n\nAdrian Boult discography: The English conductor Sir Adrian Boult was a prolific recording artist.  Unlike many musicians, he felt at home in the recording studio and was happy working without an audience.  His recording career ran from November 1920, when working with Diaghilev's Ballets Russes he recorded the ballet music, \"The Good-Humoured Ladies\", to December 1978, when he made his final recording of music by Hubert Parry.\n\nKevin Sargent (composer): Kevin Sargent is a British composer for film and television who began his career as a drummer, percussionist and keyboardist with cult dance/rock pioneers Thrashing Doves.  Signed to A&M and Elektra Records, he learnt his craft at the elbow of legendary producers Chris Thomas, Jimmy Iovine and jazz luminary Tommy Lipuma, recording three critically acclaimed albums in Los Angeles, London and New York and touring the US and Europe.  Their funky and controversial \"Jesus on the Payroll\" (1988) reached the Billboard Top Twenty dance chart.\n\nTommy LiPuma: Tommy LiPuma (July 5, 1936 – March 13, 2017) was an American music producer.  He received 33 Grammy nominations, 5 Grammy wins, and sold more than 75 million albums.  LiPuma worked with many musicians, including Barbra Streisand, Miles Davis, Bill Evans, George Benson, Phil Upchurch, Al Jarreau, Anita Baker, Natalie Cole, Claudine Longet, Dave Mason, the Yellowjackets, the Sandpipers,\n\nIndila: Adila Sedraïa (born 26 June 1984), best known by her stage name Indila, is a French singer and songwriter.  She collaborated with many musicians on vocals and songwriting prior to releasing her first single, \"Dernière danse\" (\"Last Dance\"), in December 2013, which reached the SNEP Top 2 in France.  She released her first album \"Mini World\" in February 2014.\n\nThe Aggrovators: The Aggrovators were a dub/reggae backing band in the 1970s and 1980s, and one of the main session bands of producer Bunny Lee.  The line-up varied, with Lee using the name for whichever set of musicians he was using at any time.  The band's name derived from the record shop that Lee had run in the late 1960s, Agro Sounds.  Alumni of the band included many musicians who later went on to make names for themselves in reggae music.  Legends such as Jackie Mittoo, Sly and Robbie, Tommy McCook, and Aston Barrett were all involved with the band at one point or another.  Other regular members included Carlton \"Santa\" Davis, Earl \"Chinna\" Smith, George \"Fully\" Fullwood, Ansel Collins, Bernard \"Touter\" Harvey, Tony Chin, Bobby Ellis, and Vin Gordon.  The band recorded Lee's most popular output from the 1970s, with the instrumental B-sides of Lee's single releases on the Jackpot and Justice labels generally credited to The Aggrovators and mixed by King Tubby.\n\nQuestion: Tommy LiPuma worked with many musicians, including what French singer, actress, dancer and recording artist who was popular during the 1960s and 1970s?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"musician_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the musician.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the musician.\"\n    },\n    \"professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions held by the musician.\"\n    },\n    \"popularity_period\": {\n      \"type\": \"string\",\n      \"description\": \"The period during which the musician was popular.\"\n    },\n    \"producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the producer who worked with the musician.\"\n    }\n  },\n  \"required\": [\n    \"musician_name\",\n    \"nationality\",\n    \"professions\",\n    \"popularity_period\",\n    \"producer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "musician_name": {
        "type": "string",
        "description": "The full name of the musician."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the musician."
      },
      "professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions held by the musician."
      },
      "popularity_period": {
        "type": "string",
        "description": "The period during which the musician was popular."
      },
      "producer_name": {
        "type": "string",
        "description": "The name of the producer who worked with the musician."
      }
    },
    "required": [
      "musician_name",
      "nationality",
      "professions",
      "popularity_period",
      "producer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
