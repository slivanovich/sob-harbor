{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCommunity 2: A NewOrderOnline Tribute: Community 2 is a tribute album dedicated to the work of Ian Curtis, Gillian Gilbert, Peter Hook, Stephen Morris and Bernard Sumner of the bands New Order and Joy Division that was released in 2006.\n\nNew Order discography: The discography of New Order, an English rock band, consists of ten studio albums, twelve compilation albums, three live albums, five extended plays (EPs), thirty-eight singles, twelve video releases, thirty-three music videos and a number of soundtrack appearances.  New Order were formed in 1980 by singer and guitarist Bernard Sumner, bassist Peter Hook and drummer Stephen Morris.  The group began life as a continuation of their former incarnation Joy Division.  Joy Division had disbanded after the death of the lead singer Ian Curtis.  Gillian Gilbert, who was Morris' girlfriend at the time, soon joined the group and played guitar and keyboards.\n\nRound &amp; Round (New Order song): \"Round & Round\" is a song by the English band New Order from their fifth studio album \"Technique\" (1989).  The song was written by band members Gillian Gilbert, Peter Hook, Stephen Morris and Bernard Sumner, and the album version was produced entirely by New Order.  \"Round & Round\" was re-recorded for a single release, with Stephen Hague as co-producer.\n\nStephen Morris (American football): Stephen Morris (born August 27, 1992) is an American football quarterback who is currently a free agent.  He played college football at the University of Miami, and signed with the Jacksonville Jaguars as an undrafted free agent in 2014.  Morris has also been a member of the Philadelphia Eagles and Indianapolis Colts.\n\nDoubts Even Here: \"Doubts Even Here\" is the seventh track of eight on New Order's debut album \"Movement\", released on November 13, 1981.  After the death of Joy Division singer Ian Curtis, the surviving members formed New Order with drummer Stephen Morris's girlfriend Gillian Gilbert joining five months later.  This led to a dispute over who should fill Curtis' shoes with the lead vocalist role.  All three male members were in contention, but due to Bernard Sumner's voice being significantly different from Curtis', New Order opted for him to take the role, wanting New Order's sound to be different from Joy Division's.  Ironically with this new vocalist, in addition to \"Doubts Even Here\", the first track (\"Dreams Never End\") on the first album recorded by New Order, \"Movement\", is sung by bassist Peter Hook with spoken contributions by Gillian Gilbert, reading from the Bible.  The lyrics were written by Stephen Morris.\n\nSuper Highways: Super Highways is the second album by New Order members Gillian Gilbert and Stephen Morris under the name The Other Two.  It was released in 1999 six years after their début, and a year after New Order reformed.  Four tracks were co-written by Melanie Williams, who also sang lead on two of them (\"You Can Fly\" and \"One Last Kiss\") and backing vocals on the title track.  The album was re-released in January 2010 by LTM Recordings.\n\nStephen Morris (musician): Stephen Paul David Morris (born 28 October 1957) is an English multi-instrumentalist, composer and record producer who is best known for his work with the rock band New Order and, previously, Joy Division.  He also wrote and performed in The Other Two, a band consisting of Morris and his wife, Gillian Gilbert.  Morris also participated in the New Order spin-off band Bad Lieutenant.  He is known for his precise drumming that seamlessly weaves with New Order's and Joy Division's drum machine sounds. \" Stylus Magazine\" ranked Morris No. 5 on their list of \"50 Greatest Rock Drummers of All Time\".\n\nNew Order (band): New Order are an English rock band formed in 1980, currently comprising Bernard Sumner, Stephen Morris, Gillian Gilbert, Phil Cunningham and Tom Chapman.  The band was formed in 1980 by Sumner, Morris, and Peter Hook, who were the remaining members of post-punk group Joy Division following the suicide of vocalist Ian Curtis.  They added Gilbert on keyboards later that year.\n\nStephen Morris (novel): Stephen Morris and Pilotage are two short novels by Nevile Shute; the first novels he wrote after writing poetry and short stories.  \"Stephen Morris\" was finished in 1923 while Shute was working at Stag Lane for de Havilland, and \"Pilotage\" was written in 1924.  Unpublished during his lifetime, but published by his estate in one volume as many of the characters are common to both novels.  They are set in the budding (but nascent) post-war aviation industry in Britain, and also on yachts (\"Pilotage\").\n\nCommunity: A NewOrderOnline Tribute: Community is a tribute album dedicated to the work of Ian Curtis, Gillian Gilbert, Peter Hook, Stephen Morris and Bernard Sumner of the bands New Order and Joy Division that was released in 2004.\n\nQuestion: What instrument did Stephen Morris's wife play in one of his bands?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"musician_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the musician in question.\"\n    },\n    \"wife_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the musician's wife.\"\n    },\n    \"band_information\": {\n      \"type\": \"array\",\n      \"description\": \"Details about bands the musician and his wife were both members of.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"band_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the band.\"\n          },\n          \"instruments_played_by_wife\": {\n            \"type\": \"array\",\n            \"description\": \"A list of instruments played by the wife in this band.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"required\": [\n          \"band_name\",\n          \"instruments_played_by_wife\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"instrument_in_question\": {\n      \"type\": \"string\",\n      \"description\": \"The specific instrument played by the wife that answers the question.\"\n    }\n  },\n  \"required\": [\n    \"musician_name\",\n    \"wife_name\",\n    \"band_information\",\n    \"instrument_in_question\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "musician_name": {
        "type": "string",
        "description": "The name of the musician in question."
      },
      "wife_name": {
        "type": "string",
        "description": "The name of the musician's wife."
      },
      "band_information": {
        "type": "array",
        "description": "Details about bands the musician and his wife were both members of.",
        "items": {
          "type": "object",
          "properties": {
            "band_name": {
              "type": "string",
              "description": "The name of the band."
            },
            "instruments_played_by_wife": {
              "type": "array",
              "description": "A list of instruments played by the wife in this band.",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "band_name",
            "instruments_played_by_wife"
          ],
          "additionalProperties": false
        }
      },
      "instrument_in_question": {
        "type": "string",
        "description": "The specific instrument played by the wife that answers the question."
      }
    },
    "required": [
      "musician_name",
      "wife_name",
      "band_information",
      "instrument_in_question"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
