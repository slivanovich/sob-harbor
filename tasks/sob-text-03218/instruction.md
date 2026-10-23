{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGareth Cliff: Gareth Cliff Rhydal (born August, 26 1977, Pretoria, South Africa) is a South African radio and television personality.  In January 2016 he won a court case to be reinstated as a judge on the television music competition show \"Idols South Africa\" on M-Net after being suspended for a perceived racist tweet on Social Media. .  He is also a presenter of The Hollywood Report with on 5FM.\n\nFactor X (Chile season 1): Factor X is a Chilean television music competition show, to find new singing talent; the winner of which receives a recording contract with a record label.  The first season of the show debuted in March 3, 2011, and will be aired on Thursday and Sunday.  The auditions were in January 2011 and where more than 10.000 people arrived throughout the process.  It will be hosted by Julián Elfenbein, the same host of the other recent successful talent show \"Talento Chileno\", the Chilean versión of the \"Got Talent\" franchise.  It will be the second version of this format made in Latin America after the Colombian El factor X shows, but the first to meet the new requirements of the franchise in the level of production.  The judges for this season are Zeta Bosio, Karen Doggenweiler and Tito Beltrán, with Nydia Caro as guest judge.\n\nThe X Factor (U.S. TV series): The X Factor is an American reality television music competition show created by Simon Cowell and produced by FremantleMedia North America and SYCOtv, a partnership between Cowell and Sony Music Entertainment, which aired on Fox from 2011 to 2013.  Based on the original UK show, and an addition to \"The X Factor\" franchise, the series found new singing talent (solo artists and groups ages 12 and over), drawn from public auditions, and they competed against each other for votes.  The winner was determined by the show's viewers via telephone, the Internet, and SMS text voting, and was awarded a recording contract with Cowell's record label Syco Music, worth $5 million in seasons one and two, and $1 million in season three.  America voted for the following winners: Melanie Amaro, Tate Stevens, and Alex & Sierra, respectively.\n\nX Factor (Brazilian TV series): X Factor is a Brazilian reality television music competition show created by Simon Cowell and produced by FremantleMedia and Syco Entertainment, which airs on Band, with reruns airing the following day on TNT.  The series premiered on August 29, 2016.\n\nThe X Factor (U.S. season 2): Season two of the American television music competition show \"The X Factor\" premiered on Fox on September 12, 2012, and ended on December 20, 2012.\n\nThe Voice UK (series 5): The Voice UK is a British television music competition to find new singing talent.  The fifth series began airing on 9 January 2016 on BBC One.  The series is hosted by Emma Willis and Marvin Humes, and are joined by coaches will.i.am and Ricky Wilson.  Rita Ora did not appear in this series of the show after joining \"The X Factor\" and was replaced by Boy George.  In addition, Sir Tom Jones did not return and was replaced by Paloma Faith.\n\nThe Voice UK (series 6): The Voice UK is a British television music competition to find new singing talent.  The sixth series began airing on 7 January 2017, with Emma Willis hosting the main show, and Cel Spellman presenting online spin-off show \"The V Room\".  It is the first series to air on ITV since its move from BBC One.  will.i.am returned for his sixth series as a coach, Sir Tom Jones also returned to the show after a series hiatus, replacing Paloma Faith, and Jennifer Hudson and Gavin Rossdale joined as new coaches on the show, replacing Boy George and Ricky Wilson.  Mo Adeniran won the competition and Jennifer Hudson was the winning coach and the first female coach to win the show.\n\nBoy George: Boy George (born George Alan O'Dowd; 14 June 1961) is an English singer, songwriter, DJ, fashion designer and photographer.  He is the lead singer of the Grammy and Brit Award-winning pop band Culture Club.  At the height of the band's fame, during the 1980s, they recorded global hit songs such as \"Do You Really Want to Hurt Me\", \"Time (Clock of the Heart)\" and \"Karma Chameleon\" and George is known for his soulful voice and androgynous appearance.  He was part of the English New Romantic movement which emerged in the late 1970s to the early 1980s.\n\nCollect – 12&quot; Mixes Plus: Culture Club Collect – 12\" Mixes Plus is a compilation album by British band Culture Club, first released in 1991 by Virgin for the VIP Series.  The album includes remixes and extended versions of Culture Club songs that were recorded for their first four albums (1982–1986) plus a couple of their stand-out tracks, some B-sides as well as the P. W. Botha 12\" Remix of lead singer Boy George’s solo British and European Number One single \"Everything I Own\".\n\nPop Idol: Pop Idol is a British television music competition created by Simon Fuller which ran on ITV from 2001 to 2003.  The aim of the show was to decide the best new young pop singer (or \"pop idol\") in the UK based on viewer voting and participation.  Two series were broadcast—one in 2001–2002 and a second in 2003.  \"Pop Idol\" was subsequently put on an indefinite hiatus after series judge Simon Cowell announced the launch of \"The X Factor\" in the UK in April 2004.\n\nQuestion: Who has been on a British television music competition show and was was most popular in the 80's with the pop band 'Culture Club'?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_full_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full birth name of the person.\"\n    },\n    \"stage_name\": {\n      \"type\": \"string\",\n      \"description\": \"The stage name or common name of the person.\"\n    },\n    \"band_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band the person was associated with.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The person's role in the band.\"\n        },\n        \"era_of_popularity\": {\n          \"type\": \"string\",\n          \"description\": \"The decade when the band was most popular.\"\n        }\n      },\n      \"required\": [\n        \"band_name\",\n        \"role\",\n        \"era_of_popularity\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"tv_show_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"show_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the British television music competition show the person appeared on.\"\n        },\n        \"show_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of television show.\"\n        },\n        \"series_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The specific series number of the show the person appeared in.\"\n        }\n      },\n      \"required\": [\n        \"show_name\",\n        \"show_type\",\n        \"series_number\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_full_name\",\n    \"stage_name\",\n    \"band_information\",\n    \"tv_show_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_full_name": {
        "type": "string",
        "description": "The full birth name of the person."
      },
      "stage_name": {
        "type": "string",
        "description": "The stage name or common name of the person."
      },
      "band_information": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band the person was associated with."
          },
          "role": {
            "type": "string",
            "description": "The person's role in the band."
          },
          "era_of_popularity": {
            "type": "string",
            "description": "The decade when the band was most popular."
          }
        },
        "required": [
          "band_name",
          "role",
          "era_of_popularity"
        ],
        "additionalProperties": false
      },
      "tv_show_details": {
        "type": "object",
        "properties": {
          "show_name": {
            "type": "string",
            "description": "The name of the British television music competition show the person appeared on."
          },
          "show_type": {
            "type": "string",
            "description": "The type of television show."
          },
          "series_number": {
            "type": "integer",
            "description": "The specific series number of the show the person appeared in."
          }
        },
        "required": [
          "show_name",
          "show_type",
          "series_number"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_full_name",
      "stage_name",
      "band_information",
      "tv_show_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
