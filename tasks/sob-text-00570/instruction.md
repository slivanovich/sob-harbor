{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSooo Many White Guys: Sooo Many White Guys is a podcast hosted by Phoebe Robinson.  It is produced by WNYC Studios.  As a response to the predominance of white males in comedy, the podcast features guests who are mostly non-white, non-males.  The podcast hosts women, people of color, and members of the LGBTQ community.  The podcast's guests include Lizzo, podcast executive producer Ilana Glazer, Janet Mock, Hari Kondabolu, Nia Long, Gina Rodriguez, Hasan Minhaj, Roxane Gay, and Constance Wu.\n\nWNYC Studios: WNYC Studios is a producer and distributor of podcasts and on-demand and broadcast audio.  WNYC Studios produces and distributes several podcasts including 2 Dope Queens, Death, Sex & Money, Freakonomics Radio, Snap Judgment (radio show), Here’s the Thing with Alec Baldwin, The New Yorker Radio Hour, Note to Self, On the Media, Only Human, Radiolab, More Perfect, and Nancy.  WNYC Studios is a subsidiary of New York Public Radio and is headquartered in New York City.  WNYC Studios is working to grow its portfolio of podcasts with plans to launch several more podcasts in 2017.\n\n2 Dope Queens: 2 Dope Queens is a podcast hosted by Jessica Williams of \"The Daily Show\" and Phoebe Robinson of \"Broad City\".  It is produced by WNYC Studios.  The podcast features female comedians, comedians of color, and LGBT comedians, in an effort to represent people from different backgrounds.  The podcast's guests include Naomi Ekperigin, Nore Davis, Aparna Nancherla, and Michelle Buteau.  \"2 Dope Queens\" is WNYC Studios first comedy podcast.\n\nInsane Clown Posse: Insane Clown Posse (ICP) is an American hip hop duo composed of Violent J (Joseph Bruce) and Shaggy 2 Dope (originally 2 Dope; Joseph Utsler).  Founded in Detroit in 1989, Insane Clown Posse performs a style of hardcore hip hop known as horrorcore and is known for its elaborate live performances.  The duo has earned two platinum and five gold albums.  According to Nielsen SoundScan, the entire catalog of the group has sold 6.5 million units in the United States and Canada as of 2007 .  The group has established a dedicated following called Juggalos numbering in the \"tens of thousands\".\n\nRooster Teeth Podcast: The Rooster Teeth Podcast, formerly known as the Drunk Tank, is a weekly podcast produced by Rooster Teeth.  It is hosted by Gus Sorola and features various members of Rooster Teeth's staff each week.  It is sometimes advertised as simply The \"RT Podcast\".  It was named Best Gaming Podcast by the Podcast Awards in 2012 and 2013.\n\nSnap Judgment (radio show): Snap Judgment is a weekly storytelling radio series and podcast, distributed by the WNYC Studios, and hosted by Glynn Washington.  Each episode is made up of narrative pieces on a common theme.  The program first aired in July 2010.\n\nThe New Yorker Radio Hour: The New Yorker Radio Hour is a radio show and podcast produced by \"The New Yorker\" and WNYC Studios.  It is hosted by David Remnick, who has worked as an editor at \"The New Yorker\" since 1998.  The first episode of \"The New Yorker Radio Hour\" debuted on October 24, 2015.\n\nDeath, Sex and Money: Death, Sex and Money is an interview-style podcast hosted by Anna Sale that discusses the big questions \"often left out of polite conversation.\"  The podcast launched in May 2014 and is produced by WNYC Studios.  The podcast features celebrities and experts, as well as guests with little to no name recognition.  The podcast covers the topics of finance, grief, love, and relationships.\n\nMichelle Biloon: Michelle Biloon is an American stand-up comic.  Biloon started out in Austin, Texas and, after four years, moved to Los Angeles, then on to Philadelphia, where she currently resides and regularly performs.  She has been heard on the podcasts \"2 Dope Queens\", \"Comedy Bang Bang\", and \"Doug Loves Movies.\"  She has been featured on the TV shows \"Chelsea Lately\", Comedy Central's \"Premium Blend\", \"The Late Late Show with Craig Ferguson\" and \"The Gong Show with Dave Attell\".  She also produced and starred in the popular podcast \"Walking With Michelle\" and currently produces the podcast \"THEBILOONCAST.\"\n\nNew York Public Radio: New York Public Radio (NYPR) is the owner of WNYC (AM), WNYC-FM, WNYC Studios, WQXR-FM, New Jersey Public Radio, and the Jerome L. Greene Performance Space.  Combined, New York Public Radio owns WNYC (AM), WNYC-FM, WQXR-FM, WQXW, WNJT-FM, WNJP, WNJY, and WNJO.\n\nQuestion: 2 Dope Queens, which is a podcast produced by WNYC Studios features many female comedians,such as Michelle Biloon who started out in what city?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"podcast_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the podcast.\"\n    },\n    \"podcast_producer\": {\n      \"type\": \"string\",\n      \"description\": \"The entity that produces the podcast.\"\n    },\n    \"featured_comedian\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the comedian featured on the podcast.\"\n        },\n        \"starting_city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the comedian started their career.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"starting_city\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"podcast_name\",\n    \"podcast_producer\",\n    \"featured_comedian\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "podcast_name": {
        "type": "string",
        "description": "The name of the podcast."
      },
      "podcast_producer": {
        "type": "string",
        "description": "The entity that produces the podcast."
      },
      "featured_comedian": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the comedian featured on the podcast."
          },
          "starting_city": {
            "type": "string",
            "description": "The city where the comedian started their career."
          }
        },
        "required": [
          "name",
          "starting_city"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "podcast_name",
      "podcast_producer",
      "featured_comedian"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
