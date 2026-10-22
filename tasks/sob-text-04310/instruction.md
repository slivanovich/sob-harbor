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
32nd Arkansas Infantry Regiment: May 1862 found Confederate Arkansas, with almost no organized army facing an invasion by forces under Union General Samuel R. Curtis.  In March, Major General Earl Van Dorn had been ordered to move his Army of the West, via riverboats to the east side of the Mississippi River to reinforce Confederate forces near Corinth, Mississippi, leaving the state of Arkansas with no organized Confederate forces.  Major General Thomas C. Hindman was dispatched to Arkansas to assume command of the Department of the Trans-Mississippi, arriving in Little Rock on 31 May 1862.  Earlier in the month, Confederate Brigadier General John S. Roane, who had been left in command in Little Rock by General Van Dorn, had managed to stop a Texas Cavalry Regiment that was traversing the state to join General Van Dorn in Mississippi.  This gave General Hindman one organized Cavalry Regiment to attempt to stop General Curtis's force from moving from Batesville, which had been occupied in early May, south to the state capital.  Fortunately for General Hindman, the Confederate Congress had passed a Conscription (Draft) law in April 1862.  The passage of this law had two effects that would help Hindman.  The first, the law provided a method of pressing manpower into the Confederate Army through conscription or threat of conscription.  Second, the law required that all existing Confederate regiments be re-organized, with new elections for officers, but gave the existing officers the option of resigning rather than standing for re-election.  Many of the regimental officers serving in Arkansas regiments east of the Mississippi river chose to resign and follow General Hindman back to Arkansas and assist in the raising of new forces.  This gave Hindman an officer corps around which to build his new army.

Cosimo I de' Medici, Grand Duke of Tuscany: Cosimo I de' Medici (12 June 1519 – 21 April 1574) was the second Duke of Florence from 1537 until 1569, when he became the first Grand Duke of Tuscany.

50th Independence Anniversary Commemoration Medal: The 50th Independence Anniversary Commemoration Medal (Sinhala: ස්වර්ණ ජයන්ති පදක්කම "swarna jayanthi padakkama") was a military decoration awarded by the Military of Sri Lanka to servicepersons of all actively serving ranks in both the regular and volunteer forces in commemoration of the 50th anniversary of Sri Lanka's Independence from the United Kingdom, on the 4 February 1998.  A formal recommendation from service commanders was required for the award of the medal.

Battle of Montemurlo: On 1 or 2 August 1537 (both dates are given in sources), near the Tuscan village of Montemurlo, the forces of the newly installed Duke Cosimo I of Florence defeated a hastily organized army of those who wished to overthrow the Medici and restore the Republic of Florence.  Following the battle, Cosimo's bloody vengeance on all those who opposed Medici rule effectively ended organized opposition to his family in Florence.  The victory led to the decision of Emperor Charles V to formally recognize Cosimo as Duke of Florence on 30 September 1537.

Giovanni di Bicci de' Medici: Giovanni di Bicci de' Medici (c. 1360 – February 20/28, 1429) was an Italian banker, a member of Medici family of Florence, and the founder of the Medici Bank.  While other family members, such as Chiarissimo di Giambuono de' Medici, who served in the Signoria in 1201, and Salvestro de' Medici, who was implicated in the Ciompi Revolt of 1378, are historically significant, Giovanni's founding of the family bank truly began the family's rise to power in Florence.  He was the father of Cosimo de' Medici ("Pater Patriae"), grandfather of Piero di Cosimo de' Medici, great-grandfather of Lorenzo de' Medici (the Magnificent) and great-great-great-grandfather of Cosimo I de' Medici, Grand Duke of Tuscany.

President's Inauguration Medal: The President's Inauguration Medal (Sinhala: ජනාධිපති ධූරප්‍රාප්ත පදක්කම "janādhipathi dhūraprāptha padakkama") was a decoration of the Military of Sri Lanka, granted to all regular servicepersons of the country's armed services in service on 4 February 1978, following a formal recommendation by the tri-service commanders.  The decoration commemorated the inauguration of the first executive President of Sri Lanka, J. R. Jayewardene.

Battle of Mutanchiang: The Battle of Mutanchiang (or Mudanjiang) was a large-scale military engagement fought between the forces of the Union of Soviet Socialist Republics and the Empire of Japan from August 12 to 16, 1945, as part of the Soviet invasion of Manchuria.  Due to the short nature of that campaign, this was one of the only set-piece battles that transpired before its conclusion.  During the battle, elements of the Japanese Fifth Army attempted to delay the Soviet Fifth Army and First Red Banner Army long enough to allow the bulk of the Japanese forces to retreat to more defensible positions.  Though casualties on both sides were heavy, the Red Army forces were able to break through the hastily organized Japanese defenses and capture the city ten days ahead of schedule.  Nevertheless, the Japanese defenders at Mutanchiang achieved their goal of allowing the main forces to escape.

Duke of Florence: Il Duca di Firenze, rendered in English as The Duke of Florence, was a title created in 1532 by Pope Clement VII.  There were effectively only two dukes, Alessandro de' Medici and Cosimo de' Medici, the second duke being elevated to The Grand Duke of Tuscany, causing the Florentine title to become subordinate to the greater Tuscan title.

Eleonora di Garzia di Toledo: Eleonora di Garzia di Toledo (March 1553 – 11 July 1576), more often known as "Leonora" or "Dianora", was the daughter of García Álvarez de Toledo, 4th Marquis of Villafranca, Duke of Fernandina, and the wife of Don Pietro de' Medici, a son of Cosimo I de' Medici, Grand Duke of Tuscany.  Leonora was born in Florence, where she was brought up by Cosimo and Eleanor of Toledo, her aunt and namesake.  Betrothed to their son Pietro at the age of 15, she blossomed under the wing of Pietro's older sister, the artistic patron Isabella, into a vivacious and witty beauty.  Her marriage, like Isabella's, was not a success, and she followed her mentor's example of taking lovers.  For this reason, Pietro had her brought in 1576 to the country retreat of Cafaggiolo, where he strangled her to death with a dog leash.  Cosimo's successor, Francesco I, tacitly approved the murder, and Pietro was never brought to justice for it.

Cosmo (name): Cosmo is an English/Italian male surname and given name.  It means order, decency, and beauty ; this is the English form of Cosimo, introduced to Britain in the 18th century by the Scottish nobleman the second Duke of Gordon, who named his son and successor after his friend Cosimo III de' Medici.  Notable people and fictional characters with the name include:

Question: Who gave the formal recommendation to recognize Cosimo I of Florence, the second duke, after he defeated a hastily organized army of those wishing to restore the Republic of Florence?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "recognized_entity_name": {
      "type": "string",
      "description": "The name of the person who was formally recognized."
    },
    "recognized_entity_title": {
      "type": "string",
      "description": "The title the person was recognized with."
    },
    "recognizing_authority": {
      "type": "string",
      "description": "The authority that formally recognized the person."
    },
    "recognition_date": {
      "type": "string",
      "description": "The date when the formal recognition occurred."
    },
    "event_leading_to_recognition": {
      "type": "string",
      "description": "The event that prompted the formal recognition."
    }
  },
  "required": [
    "recognized_entity_name",
    "recognized_entity_title",
    "recognizing_authority",
    "recognition_date",
    "event_leading_to_recognition"
  ],
  "additionalProperties": false
}
