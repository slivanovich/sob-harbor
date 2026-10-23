{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLaSalle Heights disaster: The LaSalle Heights disaster occurred in the early morning of March 1, 1965 in the city of LaSalle, Quebec when a gas line explosion destroyed a number of low-cost housing units.  In all, 28 people lost their lives, 39 were injured and 200 left homeless.  Most of the casualties were women and children because many men had left for work.  The casualties might have been higher had it not been the start of the month when many men left earlier than usual to pay their monthly rent at the rental office.\n\nCallum Dixon: Dixon's work in theatre includes: \"Market Boy\", \"Sing Yer Heart Out for the Lads\", \"Rosencrantz & Guildenstern Are Dead\", \"The Wind in the Willows\", \"The Day I Stood Still\", \"Somewhere\", \"The Recruiting Officer\" and \"The Hour We Knew Nothing Of Each Other\" at the National Theatre, London; \"The Bright and Bold Design\", \"Richard II\", \"Edward II\" and \"Two Shakespearean Actors\" for the RSC; \"Mr Kolpert\", \"A Real Classy Affair\", \"Faith\" and \"Mojo\" at the Royal Court, London; \"Waiting At The Water's Edge\" at the Bush, London; \"All I Want is an Ugly Sister\" at the Lilian Baylis Theatre, London; \"When We Are Rich\" at the Nuffield Theatre, Southampton; \"Deadwood\" at the Watermill Theatre, Newbury; \"The Accrington Pals\" and \"Mowgli's Jungle\" at the Octagon Theatre, Bolton; \"Drummers\" for Out of Joint and \"Telstar\" in the West End, London.  and, most recently, \"The Government Inspector\" at The Young Vic with Julian Barratt.\n\nJack Blackburn: Charles Henry \"Jack\" Blackburn (May 20, 1883 – April 24, 1942) was an American boxer and boxing trainer.  Fighting in the first half of his career as a lightweight and later a welterweight, he was known for an exceptional defense and fought many men above his weight class, including six bouts with the great Sam Langford.  He fought Joe Gans three times in no-decision bouts, defeating him once according to newspaper accounts and made good showings against Harry Lewis, Philadelphia Jack O'Brien, and Harry Greb.  He found most of his fame training 1937 World Heavyweight Champion Joe Louis, but also had a significant role in training 1926 Lightweight Champion Sammy Mandell.  He helped to train World Bantamweight Champion Bud Taylor and World Light-Heavyweight Champion John Henry Lewis.\n\nBattle of Breslau (1757): The Battle of Breslau (also known as the \"Battle on the Lohe\") was a battle fought on 22 November 1757 during the Third Silesian War (part of the Seven Years' War).  A Prussian army of 28,000 men fought an Austrian army of 84,000 men.  The Prussians held off the Austrian attack, losing 6,000 men to the Austrians 5,000 men.  But one day later the Prussians beat a retreat.  Breslau's garrison surrendered on 25 November 1757.\n\nAccrington Pals: The Accrington Pals, officially the 11th (Service) Battalion (Accrington), East Lancashire Regiment, was a pals battalion of Kitchener's Army raised in and around the town of Accrington during the First World War.\n\nBattle of Burkersdorf: The Battle of Burkersdorf was a battle fought on 21 July 1762 during the Third Silesian War (part of the Seven Years' War).  A Prussian army of 40,000 men fought an Austrian army of around 30,000 men.\n\nPals for Life: Pals For Life is a series of British World War I drama films supported by the National Lottery through the Heritage Lottery Fund.  The films tell the story of the Pals battalions during World War I, including the Accrington Pals and the Nelson Pals.  Rowbot Street, the creators and producers, was granted £48,000 funding in total to complete the films.\n\nAso Oke hat: An Aso Oke Hat (pronounced ), a type of soft fez, is a traditional Yoruba hat that is made of hand woven Aso Oke, cotton, velvet, or damask.  In the Yoruba language, this hat is called a fila.  Although these hats originated in Nigeria they are worn by many men of African descent.  Typically, the top of the hat slouches to one side, and rests above the wearer's ear.  It is commonly worn with the Yoruba formal attire, Agbada (equally made with Aso Oke, lace or cotton) or brocade dashiki suits.  Many men wear a bowler hat with the lace dashiki suit.  However, an aso oke hat or crown style kufi cap are the most common choices when wearing any other type of formal attire.\n\nThe Accrington Pals (play): The Accrington Pals is a 1981 play by Peter Whelan.  It is based on the Accrington Pals unit in the First World War and contrasts its life at the front and experiences in the 1916 Battle of the Somme with the women left behind in Accrington.\n\nBattle of the Somme: The Battle of the Somme (French: \"Bataille de la Somme\" , German: \"Schlacht an der Somme\" ), also known as the Somme Offensive, was a battle of the First World War fought by the armies of the British and French empires against the German Empire.  It took place between 1 July and 18 November 1916 on both sides of the upper reaches of the River Somme in France.  The battle was intended to hasten a victory for the Allies and was the largest battle of the First World War on the Western Front.  More than 3 million men fought in this battle and one million men were wounded or killed, making it one of the bloodiest battles in human history.\n\nQuestion: How many men fought in the battle that the 1981 play, The Accrington Pals, is based on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"play_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the play.\"\n    },\n    \"battle_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the battle the play is based on.\"\n    },\n    \"men_fought_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the number of men who fought in the battle.\"\n    },\n    \"men_fought_minimum_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The minimum number of men who fought in the battle.\"\n    }\n  },\n  \"required\": [\n    \"play_title\",\n    \"battle_name\",\n    \"men_fought_description\",\n    \"men_fought_minimum_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "play_title": {
        "type": "string",
        "description": "The title of the play."
      },
      "battle_name": {
        "type": "string",
        "description": "The name of the battle the play is based on."
      },
      "men_fought_description": {
        "type": "string",
        "description": "A description of the number of men who fought in the battle."
      },
      "men_fought_minimum_count": {
        "type": "integer",
        "description": "The minimum number of men who fought in the battle."
      }
    },
    "required": [
      "play_title",
      "battle_name",
      "men_fought_description",
      "men_fought_minimum_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
