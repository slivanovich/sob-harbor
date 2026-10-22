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
Berlin Diary: Berlin Diary (1934–1941) is a first-hand account of the rise of Nazi Germany and its road to war, as witnessed by the American journalist William L. Shirer.  Shirer, a radio reporter for CBS, covered Germany for several years until the Nazi press censors made it impossible for him to report objectively to his listeners in the United States; feeling increasingly uncomfortable, he left the country.  The identities of many of Shirer's German sources were disguised to protect these people from retaliation by the German secret police, the Gestapo.  The contents of this book provided much of the material for his landmark book "The Rise and Fall of the Third Reich".

Speed Gibson of the International Secret Police: Speed Gibson of the International Secret Police was a radio adventure series written by Virginia Cooke.  It was centered on the adventures of Speed Gibson, a fifteen-year-old pilot who, through his uncle Clint Barlow, becomes a member of the International Secret Police.  Speed was described as “a typical American boy: interested in short wave radio, aviation and most of all - The International Secret Police.”

Pierre Paoli: Pierre-Marie Paoli, also known as Lamote, (1921 - 1946) was a French agent in the Gestapo.  The Gestapo (Secret State Police) was the official secret police of Nazi Germany and German-occupied Europe.

Heinrich Müller (Gestapo): Heinrich Müller (28 April 1900; date of death unknown, but evidence points to May 1945) was a German police official under both the Weimar Republic and Nazi Germany.  He became chief of the Gestapo, the political secret state police of Nazi Germany, and was involved in the planning and execution of the Holocaust.  He was known as "Gestapo Müller" to distinguish him from another SS general also named Heinrich Müller.  He was last seen in the "Führerbunker" in Berlin on 1 May 1945 and remains the most senior figure of the Nazi regime who was never captured or confirmed to have died.

Secret police: The term secret police or covert police force refers to intelligence services or police and law enforcement agencies which engage in covert, domestic law enforcement, intelligence, and counter-intelligence operations.  The level of oversight with which they are governed varies by country and political system.  Secret police organizations are often used by totalitarian states to protect the political power of an individual dictator or an authoritarian political regime by means of systematic engagement in extrajudicial activities.  Secret police organisations are often utilised for the purposes of policing the activities of dissidents, and weakening opposition organisations.

Heinrich Baab: Heinrich Baab (born 27 July 1908-?)  was a secretary and Gestapo chief of Frankfurt at the Lindenstrasse station.  The Gestapo (Secret State Police) was the official secret police of Nazi Germany and German-occupied Europe.  After the war in Europe ended, Heinrich Baab received a sentence of life imprisonment in March 1950 for his involvement in the Final Solution as the head of Division IIB2.  He was imprisoned from 1948 to 1973.  On 6 April 1950 he was convicted of murdering 55 Jews from 1938 to 1943 and the attempted murders of 21 Jews, as well as for maltreatment of 29 Jewish prisoners in Frankfurt.  His trial was five weeks long, with 157 witnesses testifying, including some of his victims.  Heinrich Baab sent many of Frankfurt's Jews to camps from the rail station.  Baab's supervisor at the Lindenstrasse station was Oswald Poche.  Before joining the police in 1928 in Stettin, Baab was a locksmith.  Heinrich Baab's SS membership number was 306631 and his Nazi Party number was 1346669.

Gestapo: The Gestapo (] ), abbreviation of Geheime Staatspolizei, or the Secret State Police, was the official secret police of Nazi Germany and German-occupied Europe.

Eugen Schwitzgebel: Eugen Schwitzgebel (1900 – 31 October 1944, in Aarhus) was a German officer, a SS Sturmbannführer and Gestapo leader in Aarhus during the Second World War.  He was described as "short, stocky Bavarian" who was a "ruthless and impatient man who loved to terroize his subordinates".  He was killed when British airmen bombed the University of Aarhus building which was being used as the Gestapo headquarters and place for keeping the Danish archives.

List of secret police organizations: This is a list of current secret police organizations.  Fictional secret police organizations and historical secret police organizations are listed on their own respective pages.

Double Seven Day scuffle: The Double Seven Day scuffle was a physical altercation on July 7 (7/7), 1963, in Saigon, South Vietnam.  The secret police of Ngô Đình Nhu—the brother of President Ngô Đình Diệm—attacked a group of journalists from the United States who were covering protests held by Buddhists on the ninth anniversary of Diệm's rise to power.  Peter Arnett of the Associated Press (AP) was punched on the nose, and the quarrel quickly ended after David Halberstam of "The New York Times", being much taller than Nhu's men, counterattacked and caused the secret police to retreat.  Arnett and his colleague, the Pulitzer Prize-winning journalist and photographer Malcolm Browne, were later accosted by police at their office and taken away for questioning on suspicion of attacking police officers.

Question: Who was the leader of the secret police of Nazi Germany?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "leader_name": {
      "type": "string",
      "description": "The name of the individual who was the leader."
    },
    "leader_role": {
      "type": "string",
      "description": "The specific role or title of the leader within the organization."
    },
    "organization_name": {
      "type": "string",
      "description": "The name of the secret police organization."
    },
    "organization_type": {
      "type": "string",
      "description": "A general description of the type of organization."
    },
    "country_or_regime": {
      "type": "string",
      "description": "The country or political regime the organization served."
    }
  },
  "required": [
    "leader_name",
    "leader_role",
    "organization_name",
    "organization_type",
    "country_or_regime"
  ],
  "additionalProperties": false
}
