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
Battle of Utica: The Battle of Utica (c. 240 BC) was the first major engagement in the Mercenary War between Carthaginian forces and part of the combined forces of Carthage's former mercenary armies previously deployed by Carthage to conduct the First Punic War and those of rebelling Libyan cities.  The forces of Hanno the Great broke the siege of Utica.  However, they failed to prepare any meaningful defense of the city once they liberated it or to maintain proper lookouts for enemy movement.  As a result, the Carthaginian forces suffered heavy losses when the mercenary forces counter-attacked, captured the Carthaginian baggage and equipment and besieged the army of Hanno within Utica.  Hanno managed to regain his freedom of maneuver later but failed to capitalize on opportunities to engage the rebel forces under favourable conditions.  This prompted Carthage to mobilize another army under Hamilcar Barca.

Hannibal: Hannibal Barca (Punic language: 𐤇𐤍𐤁𐤏𐤋 𐤁𐤓𐤒 , "ḥnb‘l brq"; 247 – between 183 and 181 BC), was a <a href="Ancient%20Carthage">Carthaginian</a> general, considered one of the greatest military commanders in history.  His father Hamilcar Barca was the leading Carthaginian commander during the First Punic War.  His younger brothers were Mago and Hasdrubal, and he was brother-in-law to Hasdrubal the Fair.

Po Valley raid: The raid of the Po Valley in 203 BC was the culmination of a major war, carried out by the Carthaginian commander Mago, son of Hamilcar Barca, at the end of the Second Punic war between Rome and Carthage in what is now northwestern Italy.  Mago had landed at Genoa, Liguria, two years before, in an effort to keep the Romans busy to the North and thus hamper indirectly their plans to invade Carthage’s hinterland in Africa (modern Tunisia).  He was quite successful in reigniting the unrest among various peoples (Ligurians, Gauls, Etruscans) against the Roman dominance.  Rome was forced to concentrate large forces against him which finally resulted in a battle fought in the land of the Insubres (Lombardy).  Mago suffered defeat and had to retreat.  The strategy to divert the enemy’s forces failed as the Roman general Publius Cornelius Scipio laid waste to Africa and wiped out the Carthaginian armies that were sent to destroy the invader.  To counter Scipio the Carthaginian government recalled Mago from Italy (along with his brother Hannibal, who had been in Bruttium until then).  However, the remnants of the Carthaginian forces in Cisalpine Gaul continued to harass the Romans for several years after the end of the war.

Battle of Crotona: The battle or, more precisely, the battles of Croton in 204 and 203 BC were, as well as the raid in Cisalpine Gaul, the last larger scale engagements between the Romans and the Carthaginians in Italy during the Second Punic War.  After Hannibal’s retreat to Bruttium due to the Metaurus debacle, the Romans tried continuously to block his forces from gaining access to the Ionian Sea and cut his eventual escape to Carthage by capturing Croton.  The Carthaginian commander struggled to retain his hold on the last efficient port which had remained in his hands after years of fighting and was ultimately successful.

Adherbal (governor of Gades): Adherbal was a Carthaginian noble who served as the governor of Gades during the Second Punic War.  He was also a Carthaginian military commander in this war under the command of Mago Barca.  He is perhaps best known for his defeat at the Battle of Carteia which was a naval battle that occurred in 206 BC as Adherbal was attempting to flee Carthaginian Hispania.  His fleet was defeated near the ancient city of Carteia by Gaius Laelius.

Battle of the Bagradas River: The Battle of Bagradas River or "Battle on the Macar" (c. 240 BC) was fought between Carthaginian forces and part of the combined forces of Carthage's former mercenary armies during the Mercenary War which it used to conduct the First Punic War and those of rebelling Libyan cities.  After the forces of Hanno the Great were defeated at Utica, and failed to engage the mercenaries afterwards despite favorable conditions, Carthage raised a new army under Hamilcar Barca in Carthage.  Hamilcar managed to leave Carthage despite the rebel blockade of the city and cross the Bagradas river.  Rebel armies from besieging Utica and the camp guarded the bridge on the Bargradas river.  Hamilcar Barca, by brilliant maneuvering, defeated the combined rebel army.  This was the first major Carthaginian victory of the war.  A description of the battle forms one of the grandiose set-piece scenes of Gustave Flaubert's novel, Salammbo.

Hamilcar's victory with Navaras: The battle following the defection of Numidian chieftain Naravas to Hamilcar Barca was fought between Carthaginian forces commanded by Hamilcar Barca and part of the combined forces of Carthage's former mercenary armies during the Mercenary War, which Carthage had formerly employed during the First Punic War, and those of rebelling Libyan cities supporting the mercenaries.

Ancient Carthage: Carthage (Punic: 𐤒𐤓𐤕•𐤇𐤃𐤔𐤕 , "Qart-ḥadašt " "new city") was the <a href="Phoenicia">Phoenicia</a>n <a href="city-state">city-state</a> of <a href="Carthage">Carthage</a> and during the 7th to 3rd centuries BC, included its sphere of influence, the Carthaginian Empire.  The empire extended over much of the coast of North Africa as well as encompassing substantial parts of coastal Iberia and the islands of the western Mediterranean Sea.

Mago Barca: Mago, son of Hamilcar Barca, also spelled Magon, Phoenician MGN, "God sent" (243 BC – 203 BC), was a member of the Barcid family, and played an important role in the Second Punic War, leading forces of Carthage against the Roman Republic in Hispania, Gallia Cisalpina and Italy.  Mago was the third son of Hamilcar Barca, brother to Hannibal and Hasdrubal, and brother-in-law to Hasdrubal the Fair.

Hasdrubal Barca: Hasdrubal Barca (245–207 BC) was Hamilcar Barca's second son and a Carthaginian general in the Second Punic War.  He was the brother of the famous Hannibal.

Question: The raid of the Po Valley in 203 BC was the culmination of a major war, carried out by the Carthaginian commander Mago, son of Hamilcar Barca, at the end of the Second Punic war between Rome and which location, that was a Phoenician city-state, during the 7th to 3rd centuries BC?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the historical event."
    },
    "event_year": {
      "type": "integer",
      "description": "The year the event occurred."
    },
    "commander": {
      "type": "string",
      "description": "The commander who carried out the event."
    },
    "war_name": {
      "type": "string",
      "description": "The name of the major war this event was part of."
    },
    "opposing_factions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The main factions involved in the war."
    },
    "target_location_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the location that was the opposing faction."
        },
        "type": {
          "type": "string",
          "description": "The type of entity the location was (e.g., city-state)."
        },
        "period_as_city_state": {
          "type": "string",
          "description": "The historical period during which it was a city-state."
        }
      },
      "required": [
        "name",
        "type",
        "period_as_city_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_name",
    "event_year",
    "commander",
    "war_name",
    "opposing_factions",
    "target_location_details"
  ],
  "additionalProperties": false
}
