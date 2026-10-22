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
Mary Grey, Countess of Kent: Mary Grey, Countess of Kent (died 1 November 1702), "suo jure" 1st Baroness Lucas of Crudwell (née Mary Lucas), was an English peeress in her own right.

Lady Anne Clifford, 14th Baroness de Clifford: Lady Anne Clifford, Countess Dowager of Dorset, Pembroke and Montgomery, "suo jure" 14th Baroness de Clifford (30 January 1590 – 22 March 1676) was an English peeress.  In 1605 she inherited her father's ancient barony by writ and became "suo jure" 14th Baroness de Clifford.  She was a patron of literature and as evidenced by her diary and many letters was a literary personage in her own right.  She held the hereditary office of High Sheriff of Westmorland which role she exercised from 1653 to 1676.

The King's Curse: The King's Curse is a 2014 historical novel by Philippa Gregory, part of her series "The Cousins' War".  A direct sequel to "The White Princess", it follows the adult life of Margaret Pole, Countess of Salisbury, the daughter of George Plantagenet, 1st Duke of Clarence and Isabel Neville.

Elizabeth Smith-Stanley, Countess of Derby: Elizabeth Smith-Stanley, Countess of Derby ("née" Hamilton; 26 January 1753 – 14 March 1797) was an English peeress.  As the eligible eldest daughter of the 6th Duke of Hamilton, she married the 12th Earl of Derby in 1774, giving birth to three children.  Lady Derby was popular among society and considered a leader of fashion alongside the Duchess of Devonshire.

Jane Spencer, Baroness Churchill: Jane Spencer, Baroness Churchill VA ("née" Conyngham; 1 June 1826 – 24 December 1900) was an English peeress and companion of Queen Victoria.

Alice de Lacy, 4th Countess of Lincoln: Alice de Lacy, "suo jure" 4th Countess of Lincoln, "suo jure" 5th Countess of Salisbury (25 December 1270, Denbigh Castle – 2 October 1348, Barlings Abbey) was an English peeress.

Elizabeth Boyle, Countess of Guilford: Elizabeth Boyle, Countess of Guilford (née Feilding; died circa 3 September 1667) was an English peeress.  She was created 1st Countess of Guildford for life at the Restoration on 14 July 1660, which became extinct upon her death c. 3 September 1667.  She held the office of Groom of the Stole and Lady of the Bedchamber to Queen Dowager, Henrietta Maria.

Frances Hyde, Countess of Clarendon: Frances Hyde, Countess of Clarendon (25 August 1617 (baptised) – 8 August 1667), born Frances Aylesbury, was an English peeress.  As the mother of Anne Hyde, she was mother-in-law to James II and VII, the deposed king of England, Scotland, and Ireland, and the maternal grandmother of Mary II and Queen Anne.

Catherine Murray, Countess of Dunmore: Catherine Murray, Countess of Dunmore (31 October 1814, London – 12 February 1886, Inveresk), was an English peeress and promoter of Harris Tweed.

Margaret Pole, Countess of Salisbury: Margaret Pole, Countess of Salisbury (14 August 1473 – 27 May 1541), was an English peeress.  She was the daughter of George, Duke of Clarence, the brother of kings Edward IV and Richard III.  Margaret was one of two women in 16th century England to be a peeress in her own right with no titled husband.  One of the few surviving members of the Plantagenet dynasty after the Wars of the Roses, she was executed in 1541 at the command of Henry VIII, who was the son of her first cousin Elizabeth of York.  Pope Leo XIII beatified her as a martyr for the Catholic Church on 29 December 1886.

Question: Which monarchy had this English peeress executed whose adult life is depicted in the 2014 historical novel The King's Curse?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "peeress_name": {
      "type": "string",
      "description": "The full name of the English peeress whose life is depicted in the novel."
    },
    "novel_title": {
      "type": "string",
      "description": "The title of the historical novel that follows the peeress's adult life."
    },
    "execution_details": {
      "type": "object",
      "properties": {
        "monarch_name": {
          "type": "string",
          "description": "The name of the monarch who commanded the execution."
        },
        "execution_year": {
          "type": "integer",
          "description": "The year in which the peeress was executed."
        },
        "monarch_relationship_to_peeress": {
          "type": "string",
          "description": "The familial relationship of the monarch to the peeress, as described in the context."
        }
      },
      "required": [
        "monarch_name",
        "execution_year",
        "monarch_relationship_to_peeress"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "peeress_name",
    "novel_title",
    "execution_details"
  ],
  "additionalProperties": false
}
