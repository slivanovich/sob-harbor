{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThomas Savage (Shakespeare's trustee): Thomas Savage (  1552 –1611) of Rufford, Lancashire, was a member of the Worshipful Company of Goldsmiths and one of the ten seacoal-meters in London.  Together with William Leveson, he was one of two trustees used by the original shareholders of the Globe Theatre in the allocation of their shares in 1599.  He was an associate of the actor and editor of the First Folio, John Heminges, and of John Jackson, both of whom were Shakespeare's trustees in the purchase of the Blackfriars Gatehouse.  Savage amassed a considerable fortune, at the time of his death owning five houses in London and an inn called the George.\n\nPennsylvania Shakespeare Festival: The Pennsylvania Shakespeare Festival (PSF) is a professional theater company in residence at DeSales University and the Official Shakespeare Festival of the Commonwealth of Pennsylvania.  The Festival is organized as a non-profit 501(c)(3) in Pennsylvania.  Each summer, PSF produces six or more plays (often including a musical) and special one-night-only performances.  In the fall, PSF tours a Shakespeare play to schools as part of its Linny Fowler WillPower tour.  The Festival celebrated its 25th anniversary season in the summer of 2016.  Since its inception, the Festival has been attended by 850,000 people.  The acting company consists primarily of professional actors from New York and Philadelphia and who are members of Actors' Equity Association.  The plays are performed in two theaters in The Labuda Center for the Performing Arts: the 473-seat proscenium Mainstage or the 189-seat thrust Schubert Theater on the DeSales University campus in Center Valley.\n\nNicholas Brend: Nicholas Brend (c. 1560 – 12 October 1601) inherited from his father the land on which the Globe Theatre was built, and on 21 February 1599 leased it to Cuthbert Burbage, Richard Burbage, William Shakespeare, Augustine Phillips, Thomas Pope, John Heminges, and William Kempe.  He died two years later, leaving the property on which the Globe was built to his infant son, Matthew Brend, who did not come of age until 6 February 1621.\n\nJohn Heminges: John Heminges (sometimes spelled Heming or Heminge) (bapt.  25 November 1566 – 10 October 1630) was an actor in the King's Men, the playing company for which William Shakespeare wrote.  Along with Henry Condell, he was an editor of the First Folio, the collected plays of Shakespeare, published in 1623.  He was also the financial manager for the King's Men.\n\nWilliam Heminges: William Heminges (1602 – c. 1653?) , also Hemminges, Heminge, and other variants, was a playwright and theatrical figure of the Caroline period.  He was the ninth child and third son of John Heminges, the actor and colleague of William Shakespeare.\n\nHenry Condell: Henry Condell (5 September 1576 (baptised) – December 1627) was an actor in the King's Men, the playing company for which William Shakespeare wrote.  With John Heminges, he was instrumental in preparing and editing the First Folio, the collected plays of Shakespeare, published in 1623.\n\nJohn Heminges and Henry Condell Memorial: The John Heminges and Henry Condell Memorial is a memorial to the actors John Heminges and Henry Condell in the former churchyard of St Mary Aldermanbury on Love Lane, London EC2.  The memorial is made from pink granite and topped with a bust of Shakespeare.  It was built in 1896.  It has been Grade II listed since 1972.\n\nMatthew Brend: Sir Matthew Brend (6 February 1600 – 1659) inherited from his father, Nicholas Brend, the land on which the first and second Globe Theatres were built, and which Nicholas Brend had leased on 21 February 1599 for a 31-year term to Cuthbert Burbage, Richard Burbage, William Shakespeare, Augustine Phillips, Thomas Pope, John Heminges, and William Kempe.  During much of the time he was the legal owner of the Globe, Matthew Brend was underage, and his properties were managed for him by Sir Matthew Browne, John Collet, Sir John Bodley, and Sir Sigismund Zinzan.  In 1623 Brend conveyed the property on which the Globe was built to his wife, Frances, as part of her jointure.  In 1632 he was sued in the Court of Requests by the remaining original lessee, Cuthbert Burbage, and others, for an extension of their original lease.\n\nAlexander Cooke: Alexander Cooke (died February 1614) was an actor in the King's Men and the Lord Chamberlain's Men, the acting companies of William Shakespeare, John Heminges and Richard Burbage.\n\nMartin Droeshout: Martin Droeshout ( ; April 1601 – c.1650) was an English engraver of Flemish descent, whose fame rests almost completely on the fact that he made the title portrait for William Shakespeare's collected works, the First Folio of 1623, edited by John Heminges and Henry Condell, fellow actors of the Bard.  Nevertheless, Droeshout produced other more ambitious designs in his career.\n\nQuestion: John Heminges and Alexander Cooke were both actors what acting company of Shakespeare \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the actors mentioned in the question.\"\n    },\n    \"acting_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the acting company that both actors belonged to.\"\n    },\n    \"shakespeare_connection\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the acting company was associated with William Shakespeare.\"\n    }\n  },\n  \"required\": [\n    \"actor_names\",\n    \"acting_company_name\",\n    \"shakespeare_connection\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the actors mentioned in the question."
      },
      "acting_company_name": {
        "type": "string",
        "description": "The name of the acting company that both actors belonged to."
      },
      "shakespeare_connection": {
        "type": "boolean",
        "description": "Indicates if the acting company was associated with William Shakespeare."
      }
    },
    "required": [
      "actor_names",
      "acting_company_name",
      "shakespeare_connection"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
