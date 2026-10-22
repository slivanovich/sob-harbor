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
Ray Boyle: Raymond C. Boyle, known as Ray Boyle or as the screen name Dirk London (born June 28, 1925), is an American actor known principally for his sporadic role as Morgan Earp, the brother of Wyatt Earp in fifteen episodes of the ABC/Desilu Productions western television series, "The Life and Legend of Wyatt Earp," starring Hugh O'Brian in the title role.  Boyle's episodes began with "The Assassins" in 1956 and ended with "The Outlaws Cry Murder" in 1961.

James H. Kelley: James H. Kelley, also known as Dog Kelley (c .  1833 - September 8, 1912), was an American frontiersman and businessman who as the mayor of Dodge City, Kansas, briefly supervised the law-enforcement careers of such officers as the Earp and Masterson brothers: Wyatt and Morgan Earp and Bat, Ed, and James Masterson.

Gunfight at the O.K. Corral: The Gunfight at the O.K. Corral was a 30-second shootout between lawmen and members of a loosely organized group of outlaws called the Cowboys that took place at about 3:00 p.m. on Wednesday, October 26, 1881 in Tombstone, Arizona Territory.  It is generally regarded as the most famous shootout in the history of the American Wild West.  The gunfight was the result of a long-simmering feud, with Cowboys Billy Claiborne, Ike and Billy Clanton, and Tom and Frank McLaury on one side and town Marshal Virgil Earp, Special Policeman Morgan Earp, Special Policeman Wyatt Earp, and temporary policeman Doc Holliday on the other side.  All three Earp brothers had been the target of repeated death threats made by the Cowboys, who objected to the Earps' interference in their illegal activities.  Billy Clanton and both McLaury brothers were killed.  Ike Clanton claimed that he was unarmed and ran from the fight, along with Billy Claiborne.  Virgil, Morgan, and Doc Holliday were wounded, but Wyatt Earp was unharmed.  The shootout has come to represent a period of the American Old West when the frontier was virtually an open range for outlaws, largely unopposed by law enforcement officers who were spread thin over vast territories.

Earp Vendetta Ride: The Earp Vendetta Ride was a search by Deputy U.S. Marshal Wyatt Earp, leading a federal posse, for outlaw Cowboys they believed had ambushed and maimed Virgil Earp and killed Morgan Earp.  The Earp brothers had been attacked in retaliation for the deaths of three Cowboys in the Gunfight at the O.K. Corral on October 26, 1881.  From March 20 to April 15, 1882, the federal posse searched southeast Cochise County, Arizona Territory for suspects in both Virgil's and Morgan's attacks.  Several suspects had been freed by the court, owing in some cases to legal technicalities and in others to the strength of alibis provided by Cowboy confederates.  Up to this point, Wyatt had relied on the legal system to bring the Cowboys to justice.  Now he felt he had to take matters into his own hands.

Thomas Fitch Rowland Prize: The Thomas Fitch Rowland Prize is awarded by the American Society of Civil Engineers (ASCE).  It was started in 1882, and is named for Thomas Fitch Rowland, who endowed it in 1884.

O.K. Corral hearing and aftermath: The O.K. Corral hearing and aftermath was the direct result of the 30-second Gunfight at the O.K. Corral in Tombstone, Arizona Territory on October 26, 1881.  During that confrontation, Deputy U.S. Marshal and Tombstone Town Marshal Virgil Earp, Assistant Town Marshal Morgan Earp, and temporary deputy marshals Wyatt Earp and Doc Holliday shot and killed Billy Clanton, and Tom and Frank McLaury.  Billy's brother Ike, who had repeatedly threatened to kill the Earps for some time, had been present at the gunfight but was unarmed and fled.  He filed murder charges against the Earps and Doc Holliday on October 30.

Morgan Earp: Morgan Seth Earp (April 24, 1851 – March 18, 1882) was a Tombstone, Arizona Special Policeman when he helped his brothers Virgil and Wyatt and Doc Holliday confront outlaw Cowboys in the Gunfight at the O.K. Corral on October 26, 1881.  All three Earp brothers had been the target of repeated death threats made by the Cowboys who were upset by the Earps' interference in their illegal activities.  The lawmen killed Cowboys Tom and Frank McLaury and Billy Clanton.  All four lawmen were charged with murder by Billy's older brother, Ike Clanton, who had run from the gunfight.  During a month-long preliminary hearing, Judge Wells Spicer exonerated the men, concluding they had been performing their duty.

J. T. Fitch &amp; Son: J. T. Fitch & Son was an Adelaide drapery store established by John Thomas Fitch, and carried on by his son John Thomas Fitch, jr.

Thomas Fitch (politician): Thomas Fitch (January 27, 1838 – November 12, 1923) was an American lawyer and politician.  He defended President Brigham Young of The Church of Jesus Christ of Latter-day Saints and other church leaders when Young and his denomination were prosecuted for polygamy in 1871 and 1872.  He also successfully defended Virgil, Morgan, and Wyatt Earp along with Doc Holliday when they were accused of murdering Billy Clanton, and Tom and Frank McLaury during the October 25, 1881 Gunfight at the O.K. Corral.

Newton Earp: Newton Jasper Earp (October 7, 1837 – December 18, 1928) was the eldest child of Nicholas Porter Earp and Abigail Storm.  He was the half-brother of Old West lawmen Wyatt, Virgil, and Morgan Earp.

Question: How long was the trial in which Thomas Fitch defended Morgan Earp?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "defendant_name": {
      "type": "string",
      "description": "The name of the person being defended."
    },
    "defense_attorney_name": {
      "type": "string",
      "description": "The name of the attorney who provided the defense."
    },
    "trial_type": {
      "type": "string",
      "description": "The type of legal proceeding."
    },
    "duration_in_words": {
      "type": "string",
      "description": "The duration of the trial described in words."
    },
    "duration_in_months": {
      "type": "integer",
      "description": "The duration of the trial in months."
    },
    "charges": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The charges brought against the defendant."
    },
    "outcome": {
      "type": "string",
      "description": "The outcome of the trial or hearing."
    }
  },
  "required": [
    "defendant_name",
    "defense_attorney_name",
    "trial_type",
    "duration_in_words",
    "duration_in_months",
    "charges",
    "outcome"
  ],
  "additionalProperties": false
}
