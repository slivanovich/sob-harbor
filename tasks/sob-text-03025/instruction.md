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
John II of France: John II (French: "Jean II" ; 26 April 1319 – 8 April 1364), called John the Good (French: "Jean le Bon"), was a monarch of the House of Valois who ruled as King of France from 1350 until his death.

Ambroise Paré: Ambroise Paré (c. 1510 – 20 December 1590) was a French barber surgeon who served in that role for kings Henry II, Francis II, Charles IX and Henry III.  He is considered one of the fathers of surgery and modern forensic pathology and a pioneer in surgical techniques and battlefield medicine, especially in the treatment of wounds.  He was also an anatomist and invented several surgical instruments.  He was also part of the Parisian Barber Surgeon guild.

English claims to the French throne: From the 1340s to the 19th century, excluding two brief intervals in the 1360s and the 1420s, the kings and queens of England (and, later, of Great Britain) also claimed the throne of France.  The claim dates from Edward III, who claimed the French throne in 1340 as the sororal nephew of the last direct Capetian, Charles IV.  Edward and his heirs fought the Hundred Years War to enforce this claim, and were briefly successful in the 1420s under Henry V and Henry VI, but the House of Valois, a cadet branch of the Capetian dynasty, was ultimately victorious and retained control of France.  Despite this, English and British monarchs continued to prominently call themselves kings of France, and the French fleur-de-lys were included in the royal arms.  This continued until 1801, by which time France had no monarch, having become a republic.  The Jacobite claimants, however, did not explicitly relinquish the claim.

Nicolas de Blégny: Nicolas de Blégny (1652 – 1722) was a French essayist, historian and barber surgeon.  He was appointed surgeon of queen Maria Theresa of Spain in 1678, then physician of king Louis XIV in 1682.

Philip II of France: Philip II, known as Philip Augustus (French: "Philippe Auguste" ; 21 August 1165 – 14 July 1223), was King of France from 1180 to 1223, a member of the House of Capet.  Philip's predecessors had been known as kings of the Franks, but from 1190 onward, Philip became the first French monarch to style himself king of France.  The son of King Louis VII and his third wife, Adèle of Champagne, he was originally nicknamed "Dieudonné" "God-given" because he was the first son of Louis VII, born late in his father's life.  Philip was given the nickname "Augustus" by the chronicler Rigord for having extended the Crown lands of France so remarkably.

List of the last monarchs in the Americas: The Native American hereditary leaders during this time are not included.  Those that are listed as former monarchs of what is now the continental United States were heads of European seated monarchies (or Mexican monarchs, such as Agustín I of Mexico and Maximilian I of Mexico) and themselves never set foot on American soil.  Others were indigenous monarchs, such as Malietoa Tanumafili I, Tuʻi Manuʻa Elisala and Liliuokalani of Hawaii; The last monarch of each state and territory may not be the last colonial ruler (i.e. Louis XV of France is the last French monarch of Louisiana, but Napoleon Bonaparte, prior to becoming Emperor, was the last ruler of Louisiana).  Also their end of reign may not be how the US acquired these states.  One state can have more than one last monarch, since each state may have been the product of many different acquisitions by the United States.  Different claims of a foreign country are taken into account.

Charles VII of France: Charles VII (22 February 1403 – 22 July 1461), called the Victorious (French: "le Victorieux" ) or the Well-Served (French: "le Bien-Servi" ), was a monarch of the House of Valois who ruled as King of France from 1422 to his death in 1461.

Louis XVI style: Louis XVI style, frequently also called Louis Seize, is a characteristic French style in art, architecture, and decorative motif which developed during the 19-year reign of the French monarch Louis XVI (1774–1793) though it often thought to encompass nearly twice that many (1750-1800).  It saw the final phase of Rococo-style art as well as the birth of French neoclassicism and the Directoire style which followed it: whereas Rococo has become labeled as overdone and gawdy with its constant use of symmetric flourishes and excessive precise decoration, neoclassicism sought to evoke the artistic styles that were just then being rediscovered in Herculaneum and Pompeii: the straight column, the simplicity of the post-and-lintel, the architrave of the Greek temple, etc., as well as the Rousseau-inspired values of returning to nature and the view of nature as an idealized and wild but still orderly and inherently worthy model for the arts to follow.

Henry III of France: Henry III (19 September 1551 – 2 August 1589; born "Alexandre Édouard de France", Polish: "Henryk Walezy" , Lithuanian: "Henrikas Valua" ) was King of the Polish-Lithuanian Commonwealth from 1573 to 1575 and King of France from 1574 until his death.  He was the last French monarch of the House of Valois.

Henry IV of France: Henry IV (French: "Henri IV" , read as "Henri-Quatre" ] ; 13 December 1553 – 14 May 1610), also known by the epithet "Good King Henry", was King of Navarre (as Henry III) from 1572 to 1610 and King of France from 1589 to 1610.  He was the first French monarch of the House of Bourbon, a branch of the Capetian dynasty.

Question: What year was the barber surgeon who served the last French monarch of the House of Valois born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "monarch": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the monarch"
        },
        "house": {
          "type": "string",
          "description": "The royal house the monarch belonged to"
        },
        "reign_end_year": {
          "type": "integer",
          "description": "The year the monarch's reign ended"
        }
      },
      "required": [
        "name",
        "house",
        "reign_end_year"
      ],
      "additionalProperties": false
    },
    "barber_surgeon": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the barber surgeon"
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the barber surgeon"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "Description of the relationship between the barber surgeon and the monarch"
    }
  },
  "required": [
    "monarch",
    "barber_surgeon",
    "relationship_description"
  ],
  "additionalProperties": false
}
