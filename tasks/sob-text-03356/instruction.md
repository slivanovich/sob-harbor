{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichelle Tanner: Michelle Elizabeth Tanner is a fictional character on the long-running ABC sitcom \"Full House\", who was portrayed by Mary-Kate and Ashley Olsen.  She first appeared in the show's pilot, \"Our Very First Show\", which aired in 1987, and continued to appear throughout up to the two-part series finale, \"Michelle Rides Again\" in 1995.  The character of Michelle was the Olsen twins' first acting role; the two were infants when they started working on the series.\n\nShane Ramsay: Shane Ramsay is a fictional character from the Australian Network Ten soap opera \"Neighbours\", played by Peter O'Brien.  He made his first appearance on-screen in the first \"Neighbours\" episode on 18 March 1985.  Shane is the son of Max and Maria Ramsay.  His storylines included training to be an Olympic swimmer, being injured in two car crashes and his relationship with Daphne Lawrence.  Shane departed on 3 March 1987.  He appeared in 290 episodes.\n\nNot Cool (film): Not Cool is a 2014 American romantic comedy film directed, produced, and edited by Shane Dawson.  The film centers around a group of high school friends reuniting over their Thanksgiving break during college.  It is one of two films that were produced for the Starz reality competition show \"The Chair\", where the competitors use the same screenplay to create their own film.  The film stars Cherami Leigh, Shane Dawson, Drew Monson, Michelle Veintimilla, Lisa Schwartz, and Bill Laing.\n\nShane Lynch: Shane Lynch (born Shane Eamon Mark Stephen Lynch; 3 July 1976) is an Irish singer-songwriter, actor and professional drift driver, best known as a member of Boyzone.  In recent years he has taken up auto racing, participated in reality shows, and appeared as a judge on \"The All Ireland Talent Show\".\n\nShane O'Donoghue: Shane O'Donoghue is an Irish golf journalist who presents \"Living Golf\" on CNN.  From Clonmel, County Tipperary, Shane worked for RTÉ as a presenter, DJ and read the news on 2fm's \"The Full Irish\" morning/breakfast show.  A keen golfer, Shane has presented and contributed to shows for RTÉ and the BBC as part of their golf coverage, he has also worked for the European Tour World feed of its events.  Shane moved to the United States to work for CNN and has also worked for the Golf Channel and Fox.\n\nMichelle Knotek: Michelle Knotek is a former Raymond, Washington, woman who was convicted in 2004 of second-degree murder and manslaughter in the torture and deaths of Kathy Loreno and Ronald Woodworth, who were both boarders in Knotek's home.  Her husband, David Knotek, was also convicted of the murder of his 19-year-old nephew Shane Watson, who lived with the Knoteks.  Michelle is also suspected of possible involvement in the death of James McClintock, an 81 year-old whose assets she inherited after he died of head trauma incurred while Knotek was employed as his caregiver on February 9, 2002.\n\nKat Slater: Kathleen \"Kat\" Moon (also Slater) is a fictional character from the BBC soap opera \"EastEnders\", played by Jessie Wallace.  She was also played by Kate Peck in a flashback in 2001.  Kat is the daughter of Viv Slater and Charlie Slater (Derek Martin), and arrived with her sisters Lynne Hobbs (Elaine Lordan) and Little Mo Morgan (Kacey Ainsworth).  Her daughter Zoe Slater (Michelle Ryan) is initially believed to be her sister as well until Kat reveals she was raped by her uncle Harry Slater (Michael Elphick) as a child.  She later marries Alfie Moon (Shane Richie).  It is later revealed that Kat also gave birth to a son, Zoe's twin brother.  She appeared in the show from September 2000 to November 2004, then returned in May 2005 following a period of maternity leave.  She left on 25 December 2005, and returned on 17 September 2010, to leave again in January 2012 and return on 7 June 2012.  Wallace, alongside Richie, departed on-screen on 22 May 2015, returning for a short stint from 25 December 2015 to 25 January 2016, before reprising their roles as Kat and Alfie in the six-part spin-off drama series \"\", in May and June 2017.  The spin-off reveals that Kat's son is a murderous Catholic priest, Dermott Dolan (Oisín Stack) and ends on a cliffhanger where it is not known if Kat will live or die.\n\nMichelle Mitchenor: Michelle Mitchenor is an American actress.  She is known for portraying the series regular role of Detective Sonya Bailey on the FOX's primetime action comedy-drama television series Lethal Weapon and the role of Indigo in the musical-drama film Chi-Raq.\n\nVictoria and Shane Grow Their Own: Victoria and Shane Grow Their Own is an Irish reality television special which originally aired on RTÉ One on Tuesday 8 December 2009.  It follows the trials of Victoria Mary Clarke and Shane MacGowan as they endeavour to grow their own food in their own garden.  The show documents Clarke's struggles to grow vegetables and MacGowan's attempts to assist.  Filming of the special took place in Dublin.  It has been compared to the 1970s sitcom \"The Good Life\".  MacGowan is from an agricultural background.  First Lady of the United States Michelle Obama was said to have influenced the couple.\n\nLethal Weapon (TV series): Lethal Weapon is an American buddy cop action comedy-drama television series that is based on the film series of the same name created by Shane Black.  The series was ordered on May 10, 2016 and premiered on Fox on September 21, 2016.  On October 12, 2016, Fox picked up the series for a full season of 18 episodes.  On February 22, 2017, Fox renewed the series for a second season, which premiered on September 26, 2017.\n\nQuestion: Michelle Mitchenor appeared on what Shane Black-created show?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"tv_series\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the TV series.\"\n        },\n        \"creator\": {\n          \"type\": \"string\",\n          \"description\": \"The creator of the TV series.\"\n        },\n        \"network\": {\n          \"type\": \"string\",\n          \"description\": \"The network the TV series aired on.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"creator\",\n        \"network\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"character_played\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actress in the series.\"\n    },\n    \"role_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of role the actress had in the series (e.g., series regular).\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"tv_series\",\n    \"character_played\",\n    \"role_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "tv_series": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the TV series."
          },
          "creator": {
            "type": "string",
            "description": "The creator of the TV series."
          },
          "network": {
            "type": "string",
            "description": "The network the TV series aired on."
          }
        },
        "required": [
          "title",
          "creator",
          "network"
        ],
        "additionalProperties": false
      },
      "character_played": {
        "type": "string",
        "description": "The name of the character played by the actress in the series."
      },
      "role_type": {
        "type": "string",
        "description": "The type of role the actress had in the series (e.g., series regular)."
      }
    },
    "required": [
      "actress_name",
      "tv_series",
      "character_played",
      "role_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
