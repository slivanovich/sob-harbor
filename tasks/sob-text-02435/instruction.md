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
HMS Vanguard (23): HMS "Vanguard" was a British fast battleship built during the Second World War and commissioned after the war.  She was the only ship of her class, the biggest and fastest of the Royal Navy's battleships, and the last battleship to be launched in the world.  Work on the ship's design commenced before the war because the Royal Navy anticipated being outnumbered by the combined German and Japanese battleships in the early 1940s.  The British had enough 15 in guns and turrets in storage to allow one ship of a modified "Lion"-class battleship design to be completed faster than the ships of that class that had already been laid down.  Work on "Vanguard" was started and stopped several times during the war and even after construction had begun, her design was revised several times to reflect war experience.  These stoppages and changes prevented her from being completed during the war.

HMS Queen Elizabeth (R08): HMS "Queen Elizabeth" is the lead ship of the "Queen Elizabeth"-class of supercarrier, the largest warship ever built for the Royal Navy of the United Kingdom and capable of carrying up to 40 aircraft.  The ship was named by Queen Elizabeth II in July 2014, began sea trials in June 2017 and will formally be commissioned by the end of 2017.  Her first Commanding Officer is Commodore Jerry Kyd, who had previously commanded the carriers HMS "Ark Royal" and HMS "Illustrious".  As Captain of HMS "Queen Elizabeth", Kyd will wear the Royal Navy rank of Captain while retaining the substantive rank of Commodore.

HMS Valiant (1914): HMS "Valiant" was a "Queen Elizabeth"-class battleship built for the Royal Navy during the early 1910s.  She participated in the Battle of Jutland during the First World War as part of the Grand Fleet.  Other than that battle, and the inconclusive Action of 19 August, her service during the war generally consisted of routine patrols and training in the North Sea.  She saw further action during the Second World War in the Mediterranean and Far East.

HMS Barham (04): HMS "Barham" was a "Queen Elizabeth"-class battleship built for the Royal Navy during the early 1910s.  Often used as a flagship, she participated in the Battle of Jutland during the First World War as part of the Grand Fleet.  For the rest of the First World War, except for the inconclusive Action of 19 August 1916, her service during the war generally consisted of routine patrols and training in the North Sea.

Queen Elizabeth-class battleship: The "Queen Elizabeth"-class battleships were a class of five super-dreadnoughts of the Royal Navy commissioned in 1915–16.  The lead ship was named after Elizabeth I of England.  These battleships were superior in firepower, protection and speed to their Royal Navy predecessors of the "Iron Duke" class as well as preceding German classes such as the "König" class , although the corresponding "Bayern"-class ships were competitive except for being 2 kn slower.  As such, the "Queen Elizabeth"s are generally considered the first fast battleships.

HMS Queen Elizabeth (1913): HMS "Queen Elizabeth" was the lead ship of her class of dreadnought battleships built for the Royal Navy in the early 1910s, and was often used as a flagship.  She served in World War I as part of the Grand Fleet, and participated in the inconclusive Action of 19 August.  Her service during the war generally consisted of routine patrols and training in the North Sea.  She and the other super-dreadnought battleships were the first of their type to be powered by oil instead of coal.  "Queen Elizabeth" later served in several theatres during World War II, and was ultimately scrapped in 1948.

HMS Malaya: HMS "Malaya" was a "Queen Elizabeth"-class battleship built for the Royal Navy during the early 1910s.  Shortly after commissioning in 1916, she participated in the Battle of Jutland as part of the Grand Fleet.  Other than that battle, and the inconclusive Action of 19 August, her service during the First World War generally consisted of routine patrols and training in the North Sea.

HMS Queen (1902): HMS "Queen" was a "London" or "Queen" class battleship commissioned in 1904, a sub-class of the "Formidable" class battleships of the British Royal Navy.  It was the tenth Royal Navy ship to bear the name.

King George V-class battleship (1911): The "King George V"-class battleships were a group of four dreadnought battleships built for the Royal Navy (RN) in the early 1910s that were sometimes termed super-dreadnoughts.  The sister ships spent most of their careers assigned to the 2nd Battle Squadron of the Home and Grand Fleets, sometimes serving as flagships.  In October 1914, "Audacious" struck a mine and sank.  Aside from participating in the failed attempt to intercept the German ships that had bombarded Scarborough, Hartlepool and Whitby in late 1914, the Battle of Jutland in May 1916 and the inconclusive Action of 19 August, the surviving ships' service during the First World War generally consisted of routine patrols and training in the North Sea.

HMS Warspite (03): HMS "Warspite" was a "Queen Elizabeth"-class battleship built for the Royal Navy during the early 1910s.  Her thirty-year career covered both world wars and took her across the Atlantic, Indian, Arctic and Pacific Oceans.  She participated in the Battle of Jutland during the First World War as part of the Grand Fleet.  Other than that battle, and the inconclusive Action of 19 August, her service during the war generally consisted of routine patrols and training in the North Sea.

Question: HMS "Barham" was a "Queen Elizabeth"-class battleship built for the Royal Navy during the early 1910s, The "Queen Elizabeth"-class battleships were a class of how many super-dreadnoughts of the Royal Navy commissioned in 1915–16?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ship_class_name": {
      "type": "string",
      "description": "The name of the battleship class."
    },
    "ship_type": {
      "type": "string",
      "description": "The specific type of ship within the class."
    },
    "number_of_ships": {
      "type": "integer",
      "description": "The total number of ships in the class."
    },
    "commissioning_period": {
      "type": "string",
      "description": "The period during which the ships of the class were commissioned."
    }
  },
  "required": [
    "ship_class_name",
    "ship_type",
    "number_of_ships",
    "commissioning_period"
  ],
  "additionalProperties": false
}
