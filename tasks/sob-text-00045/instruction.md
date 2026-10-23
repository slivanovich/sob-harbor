{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n30-Second Bunnies Theatre: 30-Second Bunnies Theatre is a Flash cartoon series featuring films re-enacted by anthropomorphic animated bunnies in 30 seconds.  The series is produced by Angry Alien Productions, the one-woman company of creator Jennifer Shiman.\n\nJoe Cartoon: Joe Cartoon is an Adobe Flash cartoon series created by Joseph C. Shields and animated by Klasky Csupo and Mondo Media.  Starting as an independent website, Joe Cartoon was later affiliated with Atom Films, before becoming independent again in 2006, then being bought in 2007 by Endemol.\n\nMaking Fiends (web cartoon): Making Fiends is a Flash cartoon series by Amy Winfrey.  It follows the interactions between Vendetta, a villainous girl that regularly makes monsters called \"fiends\", and Charlotte, a cheerful and naive girl who thinks Vendetta is her best friend.  Charlotte unintentionally irritates and embarrasses Vendetta.  As a result, Vendetta attempts to assassinate her with fiends, but she always fails out of Charlotte's luck.\n\nXiao Xiao: Xiao Xiao () is an Internet Flash cartoon series by Chinese animator Zhu Zhiqiang, featuring stick figure men performing choreographed fight scenes.  Some of the cartoons are interactive and game-like.  All cartoons are in the Adobe Flash format, although Xiao Xiao #1 was originally in AVI format.  It has now been converted to Flash format.\n\nThe Goddamn George Liquor Program: The Goddamn George Liquor Program is a 1997 Adobe Flash cartoon series created by John Kricfalusi and starring the animated character George Liquor.  Liquor was spun out to his own web-based cartoon during the days when the Spümcø studio had an online presence.  Michael Pataki voiced Liquor in the series.  Spümcø produced eight one-minute shorts.\n\nFlash animation: A flash animation or flash cartoon is an animated film that is created with the Adobe Flash platform or similar animation software and often distributed in the SWF file format.  The term Flash animation refers to both the file format and the medium in which the animation is produced.  Flash animation has enjoyed mainstream popularity since the mid-2000s, with many Flash-animated television series, television commercials, and award-winning online shorts being produced since then.\n\nWeekend Pussy Hunt: Weekend Pussy Hunt was an Internet-only film noir cartoon series created by John Kricfalusi, starring Dirty Dog and Cigarettes the Cat.  The series was initially developed for MSN, which billed it as \"the world's first interactive web-based cartoon\" and slated it for release in 1997, but MSN stopped the production before the cartoon was finished.  In 1999 the series began airing on Icebox.com, after the release of Spümcø's own web-based Flash cartoon, \"The Goddamn George Liquor Program\".  The first scene was animated prior to Flash's acquisition by Macromedia, when the software was still called FutureSplash Animator.\n\nAglaia Mortcheva: Aglaia Mortcheva (Bulgarian: Аглая Морчева ) (born 1972) is a Bulgarian animator, illustrator and voice actress, perhaps best known for her portrayal as Vendetta on the \"Making Fiends\" web series and on the television series.\n\nThere She Is!!: There She Is!!  (Korean: 떳다 그녀!!)  is a Flash cartoon series produced by a three-person team and hosted on the Korean website SamBakZa.  The cartoons became particularly popular during the spring of 2004 when they were exposed to American and European audiences.  The series is originated from Comic strip 'One day'(Korean: 어떤날) which has been published from November 2000 until March 2002 on Braille newspaper 'Newspaper that we read together'(Hangul: 함께 읽는 신문) that is published by Korean newspaper Hankook Ilbo.  The series is noted for its classic manhwa style elements and its high-quality animation.  The first \"There she is!!\"  generated a large amount of positive feedback from its online audience, including fan art, which drove SamBakZa to produce more cartoons in the series.\n\nBadgers (animation): Badgers is a Flash cartoon by British animator Jonti Picking (aka \"Weebl\").  It consists of 12 animated cartoon badgers doing calisthenics, a toadstool in front of a tree, and a snake in the desert.  The Flash cartoon is accompanied by electronic dance music.\n\nQuestion: who wrote the Flash cartoon series inwhich Aglaia Mortcheva was  portrayed as Vendetta\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Flash cartoon series.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character portrayed by the voice actor.\"\n    },\n    \"voice_actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the voice actor.\"\n    },\n    \"creator_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the creator or writer of the series.\"\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"character_name\",\n    \"voice_actor_name\",\n    \"creator_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the Flash cartoon series."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character portrayed by the voice actor."
      },
      "voice_actor_name": {
        "type": "string",
        "description": "The name of the voice actor."
      },
      "creator_name": {
        "type": "string",
        "description": "The name of the creator or writer of the series."
      }
    },
    "required": [
      "series_name",
      "character_name",
      "voice_actor_name",
      "creator_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
