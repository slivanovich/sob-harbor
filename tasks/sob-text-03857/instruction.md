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
Fontus: In ancient Roman religion, Fontus or Fons (plural "Fontes", "Font" or "Source") was a god of wells and springs.  A religious festival called the Fontinalia was held on October 13 in his honor.  Throughout the city, fountains and wellheads were adorned with garlands.

Fasti (poem): The Fasti (Latin: "Fastorum Libri Sex" , "Six Books of the Calendar"), sometimes translated as The Book of Days or On the Roman Calendar, is a six-book Latin poem written by the Roman poet Ovid and published in 8 AD.  Ovid is believed to have left the "Fasti" incomplete when he was exiled to Tomis by the emperor Augustus in 8 AD.  Written in elegiac couplets and drawing on conventions of Greek and Latin didactic poetry, the "Fasti" is structured as a series of eye-witness reports and interviews by the first-person "vates" ("poet-prophet" or "bard") with Roman deities, who explain the origins of Roman holidays and associated customs—often with multiple aetiologies.  The poem is a significant, and in some cases unique, source of fact in studies of religion in ancient Rome; and the influential anthropologist and ritualist J.G. Frazer translated and annotated the work for the Loeb Classical Library series.  Each book covers one month, January through June, of the Roman calendar, and was written several years after Julius Caesar replaced the old system of Roman time-keeping with what would come to be known as the Julian calendar.

Jupiter (mythology): Jupiter, also known as Jove (Latin: "Iūpiter" ] or "Iuppiter" ] , gen.  "Iovis" ] ), is the god of the sky and thunder and king of the gods in Ancient Roman religion and mythology.  Jupiter was the chief deity of Roman state religion throughout the Republican and Imperial eras, until Christianity became the dominant religion of the Empire.  In Roman mythology, he negotiates with Numa Pompilius, the second king of Rome, to establish principles of Roman religion such as offering, or sacrifice.

Feriae Latinae: The Feriae Latinae or Latin Festival was an ancient Roman religious festival held in April on the Alban Mount.  The date varied, and was determined and announced by the consuls each year when they took office.  It was one of the most ancient festivals celebrated by the Roman state and is supposed to have predated the founding of Rome—in historical terms, to have dated to a pre-urban pastoral age.  It continued to be held into the 3rd century AD, and perhaps later.

Navigium Isidis: The Navigium Isidis or Isidis Navigium (trans.  "the vessel of Isis") was an annual ancient Roman religious festival in honor of the goddess Isis, held on March 5.  The festival outlived Christian persecution by Theodosius (391) and Arcadius' persecution against the Roman religion (395).

Pontifex Maximus: The Pontifex Maximus (Latin, literally: "greatest pontiff" or "greatest bridge-builder") was the high priest of the College of Pontiffs ("Collegium Pontificum") in ancient Rome.  This was the most important position in the ancient Roman religion, open only to patricians until 254 BC, when a plebeian first occupied this post.  A distinctly religious office under the early Roman Republic, it gradually became politicized until, beginning with Augustus, it was subsumed into the Imperial office.  Its last use with reference to the emperors is in inscriptions of Gratian (reigned 375–383) who, however, then decided to omit the words "pontifex maximus" from his title.  Although the most influential office within Roman priesthood, the "pontifex maximus" was ranked the fifth in the ranking of the highest Roman priests ("ordo sacerdotum"), behind the "rex sacrorum" and the "flamines maiores" ("Flamen Dialis", "Flamen Martialis", "Flamen Quirinalis").

Quinquatria: In ancient Roman religion, the Quinquatria or Quinquatrus was a festival sacred to the Goddess Minerva, celebrated from the 19-23 of March.  The older festivals were of Etruscan origin and were to celebrate the Spring Equinox, the spring rebirth rites of women.  According to Varro, it was so-called because it was held on the fifth "(quinqu-)" day after the Ides, in the same way as the Tusculans called a festival on the sixth day after the Ides "Sexatrus" or one on the seventh "Septimatrus".  Both Varro and Festus state that the Quinquatrus was celebrated for only one day, but Ovid says that it was celebrated for five days, hence the name: on the first day no blood was shed, but that on the last four there were contests of gladiators.  The first day was the festival proper, and that the following four were an expansion made perhaps in the time of Caesar to gratify the people.  The ancient Roman religious calendars assign only one day to the festival.

Fornacalia: The Fornacalia was an Ancient Roman religious festival celebrated in honour of the goddess "Fornax", a divine personification of the oven ("fornax"), and was related to the proper baking of bread.  Ovid wrote that "the oven was made a goddess, Fornax: the farmers, pleased with her, prayed she’d regulate the grain’s heat."  It was held in early February on various dates in different "curiae", which in the period of the Roman monarchy and the Roman Republic were the thirty wards of the city of Rome.  It was proclaimed every year by the "curio maximus", who was a priest who was the head of the "curiae".  He announced the different part which each "curia" (sing.  of "curiae") had to take in the celebration of the festival; "[n]ow the Curio Maximus, in a set form of words, declares the shifting date of the Fornacalia, the Feast of Ovens, and round the Forum hang many tablets, on which every ward displays its particular sign."  It is believed that every family in the curia brought "far" (spelt, a kind of grain), to be toasted in the meeting hall and sacrificed to ensure that bread in the household ovens wouldn’t be burnt in the coming year.  The last day of this festival was the "quirinalia", which was also jokingly nicknamed the 'feast of fools'.  All the curiae met together on that day for a collective feast.  Those who did not know to what curia they belonged were able to participate in its rites; "[f]oolish people don’t know which is their ward, so they hold the feast on the last possible day.  This tradition indicates that in later times membership of a curia (singular of curiae) had little significance to most Romans, so much so that some people did not which curia they belonged to; the curiae included all citizens and that every Roman citizen was deemed to belong to a curia, even if he did not know which it was."

Roman festivals: Festivals in ancient Rome were an important part of Roman religious life during both the Republican and Imperial eras, and one of the primary features of the Roman calendar.  Feriae ("holidays" in the sense of "holy days"; singular also "feriae" or dies ferialis) were either public "(publicae)" or private "(privatae)".  State holidays were celebrated by the Roman people and received public funding.  Games "(ludi)", such as the Ludi Apollinares, were not technically "feriae", but the days on which they were celebrated were "dies festi", holidays in the modern sense of days off work.  Although "feriae" were paid for by the state, "ludi" were often funded by wealthy individuals.  "Feriae privatae" were holidays celebrated in honor of private individuals or by families.  This article deals only with public holidays, including rites celebrated by the state priests of Rome at temples, as well as celebrations by neighborhoods, families, and friends held simultaneously throughout Rome

Juturna: In the myth and religion of ancient Rome, Juturna was a goddess of fountains, wells and springs, and the mother of Fontus by Janus.  Jupiter turned her into a water nymph – a Naiad – and gave her a sacred well in Lavinium, Latium, as well as another one near the temple to Vesta in the Forum Romanum.  The pool next to the second well was called Lacus Juturnae.  A local water nymph or river-god generally presides over a single body of water, but Juturna has broader powers which probably reflect her original importance in Latium, where she had temples in Rome and Lavinium, a cult of healthful waters at Ardea, and the fountain/well next to the lake in the Roman forum.  It was here in Roman legend that the deities Castor and Pollux watered their horses after bringing news of the Roman victory at the Battle of Lake Regillus in 496 BC (Valerius Maximus, I.8.1; Plutarch, Life of Aemilius Paulus, 25.2, Life of Coriolanus, 3.4).

Question: In ancient Roman religion, Fontus or Fons (plural "Fontes", "Font" or "Source") was a god of wells and springs, a religious festival called the Fontinalia was held on October 13 in his honor, festivals in ancient Rome were an important part of Roman religious life during which eras, and one of the primary features of the Roman calendar?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "deity_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the deity."
        },
        "domain": {
          "type": "string",
          "description": "The domain or aspect of nature the deity presides over."
        }
      },
      "required": [
        "name",
        "domain"
      ],
      "additionalProperties": false
    },
    "fontinalia_festival_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the festival."
        },
        "date": {
          "type": "string",
          "description": "The date on which the festival was held."
        },
        "honored_deity": {
          "type": "string",
          "description": "The deity in whose honor the festival was held."
        }
      },
      "required": [
        "name",
        "date",
        "honored_deity"
      ],
      "additionalProperties": false
    },
    "roman_festivals_general_info": {
      "type": "object",
      "properties": {
        "importance_eras": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The historical eras during which festivals were an important part of Roman religious life."
        }
      },
      "required": [
        "importance_eras"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "deity_info",
    "fontinalia_festival_info",
    "roman_festivals_general_info"
  ],
  "additionalProperties": false
}
