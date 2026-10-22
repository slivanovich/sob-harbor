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
Lion's Mound: The Lion's Mound (French: "Butte du Lion" , "Lion's Hillock/Knoll"; Dutch: "Leeuw van Waterloo" , "Lion of Waterloo") is a large conical artificial hill located in the municipality of Braine-l'Alleud (Dutch: Eigenbrakel), Belgium.  King William I of the Netherlands ordered its construction in 1820, and it was completed in 1826.  It commemorates the location on the battlefield of Waterloo where a musket ball hit the shoulder of William II of the Netherlands (the Prince of Orange) and knocked him from his horse during the battle.  It is also a memorial of the Battle of Quatre Bras, which had been fought two days earlier, on 16 June 1815.

Battle of Ligny: The Battle of Ligny (16 June 1815) was the last victory of the military career of Napoleon Bonaparte.  In this battle, French troops of the Armée du Nord under Napoleon's command, defeated part of a Prussian army under Field Marshal Prince Blücher, near Ligny in present-day Belgium.  The Battle of Ligny is an example of a tactical win and a strategic loss for the French.  While the French troops did force the enemy to retreat, the Prussian army survived and went on to play a pivotal role two days later at the Battle of Waterloo, reinforced by IV Prussian corps that had not participated in the battle at Ligny.  Had the French army succeeded in keeping the Prussian army from joining the Anglo-allied Army under Wellington at Waterloo, Napoleon might have won the Waterloo Campaign.

Battle of Waterloo: The Battle of Waterloo was fought on Sunday, 18 June 1815, near Waterloo in present-day Belgium, then part of the United Kingdom of the Netherlands.  A French army under the command of Napoleon Bonaparte was defeated by two of the armies of the Seventh Coalition: a British-led Allied army under the command of the Duke of Wellington, and a Prussian army under the command of Gebhard Leberecht von Blücher, Prince of Wahlstatt.

Arthur Wellesley, 1st Duke of Wellington: Field Marshal Arthur Wellesley, 1st Duke of Wellington, {'1': ", '2': ", '3': ", '4': "} (1 May 1769 – 14 September 1852) was an Anglo-Irish soldier and statesman who was one of the leading military and political figures of 19th-century Britain.  His defeat of Napoleon at the Battle of Waterloo in 1815 put him in the first rank of Britain's military heroes.

Battle of Redinha: The Battle of Redinha was a rearguard action which took place on March 12, 1811, during Masséna's retreat from Portugal, by a French division under Marshal Ney against a considerably larger Anglo-Portuguese force under Wellington.  Challenging the Allies with only one or two divisions, Ney's 7,000 troops were pitched against 25,000 men.  The success of Ney's action delayed the Allied advance and bought valuable time for the withdrawal of the main body of the French army.

First Battle of the Marne: The Battle of the Marne (French: Première bataille de la Marne , also known as the Miracle of the Marne, "Le Miracle de la Marne") was a World War I battle fought from 6–10 September 1914.  It resulted in an Allied victory against the German armies in the west.  The battle was the culmination of the German advance into France and pursuit of the Allied armies which followed the Battle of the Frontiers in August and had reached the eastern outskirts of Paris.  A counter-attack by six French armies and the British Expeditionary Force (BEF) along the Marne River forced the Imperial German Army to retreat north-west, leading to the First Battle of the Aisne and the Race to the Sea.  The battle was a victory for the Allies but led to four years of trench warfare stalemate on the Western Front.

Battle of Landen: The Battle of Landen (or Neerwinden), in the current Belgian province of Flemish Brabant, was a battle in the Nine Years' War, fought in present-day Belgium on 29 July 1693 between the French army of Marshal Luxembourg and the Allied army of King William III of England.  The French assaulted the Allied position three times before the French cavalry finally penetrated the allied defences and drove William's army from the field in a rout.  The battle was, however, quite costly for both sides, the French losing 9,000 men to the Allies' 14,000.  The French failed to follow up on their victory, allowing William to escape.

Battle of Wavre: The Battle of Wavre was the final major military action of the Hundred Days campaign and the Napoleonic Wars.  It was fought on 18–19 June 1815 between the Prussian rearguard, consisting of the Prussian III Corps under the command of General Johann von Thielmann (whose chief-of-staff was Carl von Clausewitz) and three corps of the French army under the command of Marshal Grouchy.  A blocking action, this battle kept 33,000 French soldiers from reaching the Battle of Waterloo and so helping in the defeat of Napoleon at Waterloo.

Battle of Solferino: The Battle of Solferino (referred to in Italy as the Battle of Solferino and San Martino) on 24 June 1859 resulted in the victory of the allied French Army under Napoleon III and Sardinian Army under Victor Emmanuel II (together known as the Franco-Sardinian Alliance) against the Austrian Army under Emperor Franz Joseph I.  It was the last major battle in world history where all the armies were under the personal command of their monarchs .  Perhaps 300,000 soldiers fought in the important battle, the largest since the Battle of Leipzig in 1813.  There were about 130,000 Austrian troops and a combined total of 140,000 French and allied Piedmontese troops.  After the battle, the Austrian Emperor refrained from further direct command of the army.

Panorama of the Battle of Waterloo: The Panorama of the Battle of Waterloo (French: "Panorama de la Bataille de Waterloo" ) is a rotunda in Belgium that houses a monumental panoramic painting depicting the Battle of Waterloo.  The neoclassical building is located immediately to the north of the Lion's Mound on the battlefield of the Battle of Waterloo in the municipality of Braine-l'Alleud in the Belgian province of Walloon Brabant.

Question: What nation was allied against the French in both the Battle of Waterloo and the Battle of Redinha?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_allied_nation": {
      "type": "string",
      "description": "The nation that was allied against the French in both specified battles."
    },
    "battles_information": {
      "type": "array",
      "description": "Details for each battle where the common allied nation fought against the French.",
      "items": {
        "type": "object",
        "properties": {
          "battle_name": {
            "type": "string",
            "description": "The name of the battle."
          },
          "french_commanders": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Commanders of the French forces in this battle."
          },
          "allied_commanders_from_nation": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Commanders from the common allied nation in this battle."
          }
        },
        "required": [
          "battle_name",
          "french_commanders",
          "allied_commanders_from_nation"
        ],
        "additionalProperties": false
      }
    },
    "number_of_matched_battles": {
      "type": "integer",
      "description": "The count of battles where the common allied nation fought against the French."
    }
  },
  "required": [
    "common_allied_nation",
    "battles_information",
    "number_of_matched_battles"
  ],
  "additionalProperties": false
}
