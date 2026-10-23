{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMonta Mino: Monta Mino (みの もんた , Mino Monta ) , born Norio Minorikawa (御法川 法男 , Minorikawa Norio , born 22 August 1944) , is a Japanese television presenter.  Mino is recognized by the Guinness World Records as being the TV host with the most hours of live TV appearances in a week (22 hours, 15 seconds), as of April 2008.  This breaks his earlier 2006 record of 21 hours, 42 minutes.\n\nA. J. Benza: Alfred Joseph “A.J.” Benza (born June 2, 1962) is an American gossip columnist and television host.\n\nRico J. Puno: Enrico de Jesus Puno (born 13 February 1953), better known as Rico J. Puno, is a popular Filipino pop singing artist and television host who is credited as a pioneer-promoter of original Filipino music.  He started the trend of incorporating Tagalog lyrics in his rendition of the American song \"The Way We Were\" and other foreign songs.  Also known as \"Rico J.\" and as \"The Total Entertainer\", Puno became known as a singer who regularly infused his on-stage performance with tongue-in-cheek comedy and adult humor.  He hosted the noontime variety show \"Pilipinas Win na Win\" alongside Rey Valera, Marco Sison and Nonoy Zuniga for two months in 2010 replacing Kris Aquino.  He also hosted on Happy Yipee Yehey together with John Estrada, Randy Santiago, Mariel Rodriguez, Pokwang and Toni Gonzaga as one of the main host replacing Pilipinas Win na Win.\n\nAndy Sheppard (broadcaster): Andy Sheppard (born 1972 in Simcoe, Ontario, Canada) is a Canadian broadcaster and musician.  He was the host of the defunct CBC Radio 2's nightly jazz program \"After Hours\" and currently produces and is a regular guest host of the contemporary music program \"The Signal\" for CBC Radio 2.\n\nTom Barnard: Thomas 'Tom' Mark Paul Barnard (born November 7, 1951) is an American talk radio host and former voice-over talent.  He is currently the host of \"The KQ92 Morning Show\" from 5:40am to 10:00am on 92 KQRS and Tom Barnard Show on 105 The Ticket from 6:00pm to 7:00pm both broadcast in the Minneapolis-St.  Paul area.  The show on 105 The Ticket makes up the third hour of the \"The Tom Barnard Podcast\" known as \"The Ticket\" where the first two hours of the podcast is known as \"The Show\".  As of February, 2014, the podcast was no longer broadcast on 105 The Ticket\n\nAnne Petrie: Anne Petrie (born December 24, 1946) is an award-winning broadcaster and was most known as the host of \"Canada Live\" and \"Coast to Coast\" on CBC Newsworld during its early years.  Prior to that she was the primary news anchor and host of CBWT's \"24Hours LateNight\" from October 1985 to July 1989.\n\nJ Farell: Justin Farell Alamar (born April 23, 1982), better known as J Farell, is an American music producer from Cherry Hill, NJ.  He graduated from Rutgers University where he was first exposed to music production.  J Farell broke into the recording industry in 2010 and is best known for producing remixes for artists such as Kreayshawn, J. Cole, Roscoe Dash, Gorilla Zoe, Hyper Crush, Gotye, Driicky Graham, Rita Ora, Wiz Khalifa, Eva Simons, Bruno Mars, Ed Sheeran, and more.  He received his first official placement with Entertainment One for the remix of Gorilla Zoe's song \"Twisted\".  In March 2011, it debuted on Philadelphia's radio station Wired 96.5.  This remix was digitally released on iTunes by Atlantic Records on May 23, 2011.  J Farell first received widespread recognition on August 29, 2011 when his remix of Kreayshawn's single \"Gucci Gucci\" went viral on YouTube and gained over 7 million views in under 12 hours.  A week later, the video charted at #7 on YouTube's Top 100 Music Videos.  In 2013, Ed Sheeran spoke about J Farell's remix of his song The A Team with Ralphie Aversa on WPLJ's The Ralphie Radio Show.  J Farell began working on a collaboration project with Dj Beatstreet and Dj Suraci.  In May 2015, the trio formed the group Money Drop and, two months later, released their first collaborative single entitled Everything on Fleek.  With the help of Interscope Records in July 2015, J Farell landed the official remix of Good For You by Selena Gomez featuring A$AP Rocky.  In November 2015, J Farell collaborated with singer/songwriter Todd Carey and created a refreshed, doo-wop style remix of Todd's single \"OMG\".  On December 4, 2015, the official OMG Remix was released to a positive response on social media.  His work is noted by an announcer or a giggling woman saying the \"J Farell\" tagline in most of his recent music.\n\nLisa Ling: Lisa J. Ling (born August 30, 1973) is an American journalist, television presenter, and author.  She is currently the host of \"This Is Life with Lisa Ling\" on CNN.  She is the former host of \"Our America with Lisa Ling\" on OWN: The Oprah Winfrey Network, former co-host of ABC's \"The View\" (from 1999–2002), host of \"National Geographic Explorer\", reporter on Channel One News, and special correspondent for \"The Oprah Winfrey Show\" and CNN.  She was the host of reality television show \"The Job\".  Ling is the older sister of journalist Laura Ling.\n\nA. J. After Hours: A. J.  After Hours is a television program that aired on the E! cable network in 2001.  The talk show, hosted by gossip columnist A. J. Benza, was described as a show that \"mixes interviews with comedy sketches and man-on-the-street segments, and which explores the New York's hip club scene.\"\n\nR. Brandon Johnson: Richard Brandon Johnson (born in Bloomington, Minnesota) (often credited as Brandon Johnson), known as R. Brandon Johnson, is an American actor and TV host.  He guest starred as dance show host Gary Wilde on the Disney Channel original series \"Shake It Up\" and host of TNT reality competition 72 Hours.\n\nQuestion: When was the host of A. J. After Hours born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"host_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television host.\"\n    },\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television program.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The full birth date of the host.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the host.\"\n    },\n    \"birth_month_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the birth month of the host.\"\n    },\n    \"birth_day\": {\n      \"type\": \"integer\",\n      \"description\": \"The day of the month the host was born.\"\n    }\n  },\n  \"required\": [\n    \"host_name\",\n    \"show_name\",\n    \"birth_date\",\n    \"birth_year\",\n    \"birth_month_name\",\n    \"birth_day\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "host_name": {
        "type": "string",
        "description": "The name of the television host."
      },
      "show_name": {
        "type": "string",
        "description": "The name of the television program."
      },
      "birth_date": {
        "type": "string",
        "description": "The full birth date of the host."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the host."
      },
      "birth_month_name": {
        "type": "string",
        "description": "The name of the birth month of the host."
      },
      "birth_day": {
        "type": "integer",
        "description": "The day of the month the host was born."
      }
    },
    "required": [
      "host_name",
      "show_name",
      "birth_date",
      "birth_year",
      "birth_month_name",
      "birth_day"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
