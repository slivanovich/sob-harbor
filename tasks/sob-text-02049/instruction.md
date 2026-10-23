{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBattle of Leuthen: In the Battle of Leuthen, fought on 5 December 1757, Frederick the Great's Prussian army used maneuver and terrain to decisively defeat a much larger Austrian force commanded by Prince Charles of Lorraine and Count Leopold Joseph von Daun, thus ensuring Prussian control of Silesia during the Third Silesian War (part of the Seven Years' War).\n\nBattle of Meissen: The Battle of Meissen (4 December 1759) was an Austrian victory over a larger Prussian army during the Third Silesian War (part of the Seven Years' War).  An Austrian force under the command of general Beck assaulted 3,500 Prussian troops under Diericke at Meissen, overwhelming them and driving the survivors across the Elbe.  The Prussians lost 400 men in the action and 1,543 fell prisoner.  Austrian losses were few, totalling only 72 killed and 115 wounded.  The Austrians secured an important victory, which effectively kept their ally Saxony in the war.\n\nBattle of Kunersdorf: The decisive Battle of Kunersdorf occurred on 12 August 1759 near Kunersdorf (Kunowice), immediately east of Frankfurt an der Oder (the second largest city in Prussia).  Part of the Third Silesian War and the wider Seven Years' War, the battle involved over 100,000 men.  An Allied army commanded by Pyotr Saltykov and Ernst Gideon von Laudon that included 41,000 Russians and 18,500 Austrians defeated Frederick the Great's army of 50,900 Prussians.\n\nBattle of Rossbach: The Battle of Rossbach took place on 5 November 1757 during the Third Silesian War (1756–1763, part of the Seven Years' War) near the village of Rossbach (Roßbach), in the Electorate of Saxony.  It is sometimes called the Battle of, or at, Reichardtswerben, after a different nearby town.  In this 90-minute battle, Frederick the Great, king of Prussia, defeated an Allied army composed of French forces augmented by a contingent of the Reichsarmee (Imperial Army) of the Holy Roman Empire.  The French and Imperial army included almost 42,000 men, opposing a considerably smaller Prussian force of 22,000.  Despite overwhelming odds, Frederick employed rapid movement, flanking maneuver and oblique order to achieve complete surprise.\n\nTreaty of Hubertusburg: The Treaty of Hubertusburg (German: \"Frieden von Hubertusburg\" ) was signed on 15 February 1763 at Hubertusburg Castle by Prussia, Austria and Saxony to end the Third Silesian War.  Together with the Treaty of Paris, signed five days earlier, it marked the end of the Seven Years' War.  The treaty ended the continental conflict with no significant changes in prewar borders.  Austria and Saxony renounced all claims to the Silesian territories ceded to Prussia in the 1742 Treaty of Berlin and the 1745 Treaty of Dresden.  Prussia clearly stood among the ranks of the European great powers, while the treaty enhanced the rivalry with Austria.\n\nBattle of Torgau: In the Battle of Torgau on 3 November 1760, King Frederick the Great's Prussian army fought a larger Austrian army under the command of Field Marshal Leopold Josef Graf Daun.  The Prussians won a costly victory in one of the bloodiest battles of the Third Silesian War (part of the Seven Years' War).\n\nBattle of Hochkirch: The Battle of Hochkirch occurred on 14 October 1758 during the Third Silesian War (part of the Seven Years' War).  After several weeks of maneuvering for position, an Austrian army of 80,000 commanded by Lieutenant Field Marshal Leopold Josef Graf Daun surprised the Prussian army of 30,000–36,000, commanded by Frederick the Great.  The Austrian army overwhelmed the Prussians and forced a general retreat.  The battle took place in and around the village of Hochkirch, 9 km east of Bautzen, Saxony.\n\nSilesian Wars: The Silesian Wars (German: \"Schlesische Kriege\" ) were a series of three wars fought in the mid-18th century between Prussia (under King Frederick the Great) and Austria (under Empress Maria Theresa) for control of Silesia, all three of which ended in Prussian victory.  The First (1740–42) and Second (1744–45) Silesian Wars formed a part of the larger War of the Austrian Succession, while the Third Silesian War (1756–63) was one theater of the Seven Years' War.\n\nBattle of Peterswalde: The Prussian Bohemia Incursion was a military campaign led by the Prince Henry of Prussia during the Third Silesian War (part of the Seven Years' War), to disrupt the Austrian military capacity by launching incursions against its military infrastructure in Bohemia.\n\nThird Silesian War: The Third Silesian War was a theatre of the Seven Years' War.  The name is used to describe Prussia's war against Austria and its allies between 1756 and 1763, fought mainly in Silesia, Bohemia and Upper Saxony.  The war was the third and last in a series of Silesian Wars fought between Frederick the Great's Prussia and Maria Theresa's Austria; like the earlier two, it ended with Prussia in control of the region of Silesia.\n\nQuestion: The Battle of Peterswalde, which occurred during the Third Silesian War, was a part of which larger European war?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"battle_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific battle.\"\n    },\n    \"silesian_war_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Silesian War during which the battle occurred.\"\n    },\n    \"larger_conflict_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the larger European conflict that encompassed the Silesian War.\"\n    },\n    \"conflict_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the larger conflict.\"\n    }\n  },\n  \"required\": [\n    \"battle_name\",\n    \"silesian_war_name\",\n    \"larger_conflict_name\",\n    \"conflict_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "battle_name": {
        "type": "string",
        "description": "The name of the specific battle."
      },
      "silesian_war_name": {
        "type": "string",
        "description": "The name of the Silesian War during which the battle occurred."
      },
      "larger_conflict_name": {
        "type": "string",
        "description": "The name of the larger European conflict that encompassed the Silesian War."
      },
      "conflict_type": {
        "type": "string",
        "description": "The type of the larger conflict."
      }
    },
    "required": [
      "battle_name",
      "silesian_war_name",
      "larger_conflict_name",
      "conflict_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
