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
Bender Uprising: The Bendery Uprising of 1919 was an armed uprising by Bolsheviks and their working-class allies in the city of Bendery.  It targeted the recent union of Bessarabia with the Kingdom of Romania and sought the establishment of Soviet power in the region.  It began at dawn on May 27.  The insurgents, together with a small Red Army unit that had been sent from across the Dniester River, captured the treasury building, the railroad station, and other points in the city.  Part of the occupying forces stationed in the city, consisting of French and Romanian soldiers, supported the insurgents.  By evening the same day, the command staff of the interventionist forces succeeded in suppressing the uprising.

Boudica: Boudica or Boudicca ( , Latinised as Boadicea or Boudicea , and known in Welsh as Buddug ] ) was a queen of the British Celtic Iceni tribe who led an uprising against the occupying forces of the Roman Empire in AD 60 or 61, and died shortly after its failure.  She is sometimes considered a British folk hero.

Jan Tyssowski: Jan Tyssowski (March 8, 1811 – April 5, 1857), born in Tarnów, Poland, was a Dictator of the Republic of Kraków during the failed 1846 uprising.  He was a Polish intellectual and activist during Poland's rebellions against its occupying powers.  He studied philosophy and law at the University of Lwow.  After the failed 1831 November Uprising, Russian authorities prohibited his return to Lwow, and he went study at the University of Vienna.  He was a Polish political organizer in Galicia with Ludwik Mieroslawski, and was active within the aristocracy and insurrectionist movement.  In 1846, Krakow revolted against the Austrians and they withdrew, leaving the Polish-controlled Republic of Krakow in Tyssowski's hands.  The government had originally been established as a triumvirate between Tyssowski and two others, but personal differences led Tyssowski to take control.  Intending a "classless society", he declared universal suffrage, emancipation of the peasantry, and the discontinuation of rents for peasants.  The Republic attempted to expand into neighboring rural areas, and sympathetic peasants did join the cause, but these units were defeated by much larger Austrian armies, which also had broad support among the peasants.  On March 3, Russia occupied the city and passed it back to Austria.  Roughly 1,200 people were arrested and approximately 100 were imprisoned in the Kufstein Fortress.  The Austrian Empire captured Tyssowski who surrendered to the occupying forces, and allowed him to emigrate.

Boadicea (disambiguation): Boadicea was the queen of the British Iceni tribe who led an uprising against the forces of the Roman Empire.  The name may also refer to:

Prasutagus: Prasutagus was king of a British Celtic tribe called the Iceni, who inhabited roughly what is now Norfolk, in the 1st century AD.  He is best known as the husband of Boudica.

Battle of Camulodunum: The Battle of Camulodunum, also known as the Massacre of the Ninth Legion, (60 or 61 AD) was the major military victory of the Iceni and their allies over an organised Roman army during the revolt of Boudica against the Roman occupation of Britain.  A large vexillation of the "Legio IX Hispana" were destroyed by the rebels.  Attempting to relieve the besieged "colonia" of Camulodunum (Colchester, Essex), legionaries of the Legio IX Hispana led by Quintus Petillius Cerialis, were attacked by a horde of British tribes, led by the Iceni.  Possibly 80% of the Roman foot-soldiers were killed in the battle.  The event is recorded by the historian Tacitus in his "Annals".

Bellum Batonianum: The Bellum Batonianum (Latin for "war of the Batos") was a military conflict fought in the Roman province of Illyricum in which an alliance of the native peoples of Illyricum rebelled against the Romans.  The name Batonianum holds some similarity to early Bosnian name Bestonensis and Illyrian state Bossona.  There were two regions in this Roman province: Dalmatia and Pannonia.  The rebellion began among native peoples who were recruited as auxiliary troops for the Romans.  They were led by Bato the Daesitiate (the Deasitiae were a tribe which lived in Dalmatia).  They were joined by the Breuci (a tribe in Pannonia) led by Bato the Breucan.  Many other tribes in Illyria also joined the revolt.  The Roman called this conflict bellum batonianum (Batonian war) after these two leaders who had the same name.  Velleius Paterculus called it the Pannonian and Dalmatian war because it involved both regions of Illyricum.  In English it has been called the "Great Illyrian revolt", "Pannonian-Dalmatian uprising" and "Bato uprising."  This four-year war, which lasted from 6 AD to 9 AD, saw a large deployment of Roman forces in the province, with whole armies operating across the western Balkans and fighting on more than one front.  In 8 AD the Breuci of the Sava valley surrendered, but it took another winter blockade and a season of fighting before the surrender in Dalmatia came in 9 AD .  The Roman historian Suetonius described this war as the most difficult conflict faced by Rome since the Punic Wars two centuries earlier.

Catus Decianus: Catus Decianus was the procurator of Roman Britain in AD 60 or 61.  Tacitus blames his "rapacity" in part for provoking the rebellion of Boudica.  Cassius Dio says he confiscated sums of money which had been given by the emperor Claudius to leading Britons, declaring them to be loans to be repaid with interest.

Boadicea and Her Daughters: Boadicea and Her Daughters is a bronze sculptural group in London featuring Boudica, queen of the Celtic Iceni tribe who led an uprising in Roman Britain.  It is located to the north side of the western end of Westminster Bridge, near Portcullis House and Westminster Pier, facing Big Ben and the Palace of Westminster across the road.  It is considered the "magnum opus" of its sculptor, the English artist and engineer Thomas Thornycroft.  Thornycroft worked on it from 1856 until shortly before his death in 1885, sometimes assisted by his son William Hamo Thornycroft, but it was not erected in its current position until 1902.

Camulodunum: Camulodunum ( or ; Latin: ' ), the Ancient Roman name for what is now Colchester in Essex, was an important town in Roman Britain, and the first capital of the province.  It is claimed to be the oldest town in Britain.  Originally the site of the Brythonic-Celtic oppidum of Camulodunon (meaning ""The Stronghold of Camulos""), capital of the Trinovantes and later the Catuvellauni tribes, it was first mentioned by name on coinage minted by the chieftain Tasciovanus sometime between 20 and 10 BC.  The Roman town began life as a Roman Legionary base constructed in the AD 40s on the site of the Brythonic-Celtic fortress following its conquest by the Emperor Claudius.  After the early town was destroyed during the Iceni rebellion in 60/1 AD, it was rebuilt, reaching its zenith in the 2nd and 3rd centuries.  During this time it was known by its official name Colonia Claudia Victricensis (" "), often shortened to Colonia Victricensis"', and as "Camulodunum", a Latinised version of its original Brythonic name.  The town was home to a large classical Temple, two theatres (including Britain's largest), several Romano-British temples, Britain's only known chariot circus, Britain's first town walls, several large cemeteries and over 50 known mosaics and tessellated pavements.  It may have reached a population of 30,000 at its height.  It wasn't until the late 18th century that historians realised that Colchester's physical Brythonic (British Celtic) and Roman remains were the city mentioned in ancient literature as "Camulodunum".

Question: Catus Decianus, was involved in provoking the rebellion of what queen of the British Celtic Iceni tribe who led an uprising against the occupying forces of the Roman Empire in AD 60 or 61?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rebellion_leader_name": {
      "type": "string",
      "description": "The name of the queen who led the rebellion."
    },
    "tribe_name": {
      "type": "string",
      "description": "The name of the British Celtic tribe the queen belonged to."
    },
    "target_empire": {
      "type": "string",
      "description": "The empire against which the uprising was led."
    },
    "rebellion_years": {
      "type": "array",
      "items": {
        "type": "integer"
      },
      "description": "The year or years in which the rebellion occurred."
    },
    "provoker": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual involved in provoking the rebellion."
        },
        "role": {
          "type": "string",
          "description": "The role of the individual in the Roman administration."
        },
        "provocation_factor": {
          "type": "string",
          "description": "The specific factor attributed to the individual for provoking the rebellion."
        }
      },
      "required": [
        "name",
        "role",
        "provocation_factor"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "rebellion_leader_name",
    "tribe_name",
    "target_empire",
    "rebellion_years",
    "provoker"
  ],
  "additionalProperties": false
}
