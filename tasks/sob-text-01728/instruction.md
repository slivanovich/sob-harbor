{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEdwardes baronets: The Edwardes Baronetcy, of Shrewsbury in the County of Shropshire, was a title in the Baronetage of England.  It was created on 21 March 1645 for Thomas Edwardes.  It was recreated on 22 April 1678 for his son and successor Francis Edwardes, with special remainders and precedence back to 1645, possibly due to the loss of the original patent.  Sir Francis, the 2nd Baronet was Member of Parliament for Shrewsbury 1685-90.  In 1734 the 3rd Baronet was succeeded by his cousin Henry (grandson of Thomas Edwardes, a younger son of the first Baronet) who married Eleanor Edwardes daughter of the 3rd Baronet.  In 1790 the 6th Baronet was succeeded by Reverend Thomas Edwardes, Rector of Frodesley, Shropshire, great grandson of the 1st Baronet by his 5th son.  The 7th Baronet was also Rector of Frodesley.  The titles became extinct on the death of the 10th Baronet in 1900.\n\nGlorious Revolution: The Glorious Revolution, also called the Revolution of 1688, was the overthrow of King James II of England (James VII of Scotland) by a union of English Parliamentarians with the Dutch stadtholder William III, Prince of Orange.  William's successful invasion of England with a Dutch fleet and army led to his ascension to the throne as William III of England jointly with his wife, Mary II, James's daughter, after the Declaration of Right, leading to the Bill of Rights 1689.\n\nSir Jonathan Trelawny, 3rd Baronet: Sir Jonathan Trelawny, 3rd Baronet (24 March 1650 – 19 July 1721) was a British Bishop of Bristol, Bishop of Exeter and Bishop of Winchester.  Trelawny is best known for his role in the events leading up to the Glorious Revolution which are referenced in the Cornish anthem \"The Song of the Western Men\".\n\nSir Thomas Burnett, 3rd Baronet: Sir Thomas Burnett of Leys, 3rd Baronet, (ca. 1658 – January 1714), Lord Clerk Register, PC, MP.  He was, at Stonehaven, 21 April 1664, retoured as heir to his father, Sir Alexander Burnett, 2nd Baronet who had died the previous year.  The 3rd Baronet is the grandson of Sir Thomas Burnett, 1st Baronet, who completed the reconstruction of Muchalls Castle and the great-grandson of Alexander Burnett of Leys (died 1619), who completed the construction of Crathes Castle.\n\nJohn Trelawny (died 1680): Captain John Trelawny (c.1646 – 14 May 1680) was an English army officer of Cornish descent, the eldest son of Sir Jonathan Trelawny, 2nd Baronet.\n\nSir Jonathan Trelawny, 2nd Baronet: Sir Jonathan Trelawny, 2nd Baronet (ca. 1623 – 5 March 1681), of Trelawny in the parish of Pelynt in Cornwall, England, was a Member of Parliament.\n\nJonathan Trelawny (High Sheriff of Cornwall): Sir Jonathan Trelawny (17 December 1568 – 21 June 1604), of Pool in Menheniot, Cornwall, was an English Member of Parliament.  Trelawny was the posthumous younger son of John Trelawny of Pool (who had been a member of parliament and High Sheriff of the county); his elder brother died in infancy and he inherited the estate.  He entered Parliament as member for Liskeard, representing that borough in three parliaments, and subsequently also represented Cornwall in the Parliaments of 1597 and 1604.  On one occasion he was sent to the Tower of London for losing his temper during a parliamentary debate where he \"\"dealt his opponent, Mr Ashe, a thundering box to his ear\"\" and \"\"flashed his sword\"\".\n\nSir James Hall, 4th Baronet: Sir James Hall of Dunglass, 4th Baronet FRS FRSE (17 January 1761 – 23 June 1832) was a Scottish geologist and geophysicist, born at Dunglass, East Lothian, to Sir John Hall, 3rd Baronet (died 1776), by his spouse, Magdalen (died 1763) daughter of Sir Robert Pringle, 3rd Baronet, of Stichill, Roxburghshire.  Sir James was also Member of Parliament for St. Michael's borough (Mitchell, Cornwall) 1807–1812.\n\nCharles Trelawny: Major General Charles Trelawny (1653 – 24 September 1731) was a British Army officer of Cornish descent, the fourth son of Sir Jonathan Trelawny, 2nd Baronet.\n\nDolben baronets: The Dolben Baronetcy, of Finedon in the County of Northamptonshire, was a title in the Baronetage of England.  It was created on 1 April 1704 for Gilbert Dolben, son of John Dolben, Archbishop of York.  Gilbert was judge of the Court of Common Pleas (Ireland) and MP for Ripon, Peterborough and Yarmouth, Isle of Wight.  The 3rd Baronet was an MP for Oxford University and Northamptonshire, and was an avid campaigner for abolition of the slave trade.  The title became extinct on the death of Sir John English Dolben, the 4th Baronet, in 1837.  William Harcourt Isham Mackworth (1806—1872), a younger son of Sir Digby Mackworth, the 3rd Baronet, took the additional surname Dolben after he married Frances, the heiress of the 4th Baronet.\n\nQuestion: Which king was overthrown by Sir Jonathan Trelawny, 3rd Baronet's revolution?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"revolution_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the revolution.\"\n    },\n    \"overthrown_king\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the king who was overthrown during the revolution.\"\n    },\n    \"king_titles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other titles or names associated with the overthrown king.\"\n    },\n    \"key_figure\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the key figure associated with the revolution.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the key figure (e.g., Baronet).\"\n        },\n        \"role_in_revolution\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the key figure's involvement in the revolution.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title\",\n        \"role_in_revolution\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"revolution_name\",\n    \"overthrown_king\",\n    \"king_titles\",\n    \"key_figure\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "revolution_name": {
        "type": "string",
        "description": "The name of the revolution."
      },
      "overthrown_king": {
        "type": "string",
        "description": "The name of the king who was overthrown during the revolution."
      },
      "king_titles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other titles or names associated with the overthrown king."
      },
      "key_figure": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the key figure associated with the revolution."
          },
          "title": {
            "type": "string",
            "description": "The title of the key figure (e.g., Baronet)."
          },
          "role_in_revolution": {
            "type": "string",
            "description": "Description of the key figure's involvement in the revolution."
          }
        },
        "required": [
          "name",
          "title",
          "role_in_revolution"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "revolution_name",
      "overthrown_king",
      "king_titles",
      "key_figure"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
