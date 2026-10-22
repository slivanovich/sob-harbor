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
Kichhhu Sanlap Kichhu Pralap: Kichhhu Sanlap Kichhu Pralap (English: Dialogue and Delirium ) is a 1999 Indian Bengali drama film directed and produced by Ashoke Viswanathan, starting Ashoke Viswanathan, Sanjiban Guha and Nandini Ghosal in the lead roles.  Screenplay written by Ashoke Viswanathan collaboratively with Shankar Bhaterjee, Prhalad Chattopadhay and Mrinmoy nandi.

Radha Jayalakshmi: Radha and Jayalakshmi, popularly known as Radha Jayalakshmi (Tamil: ராதா ஜெயலட்சுமி ), were Indian Carnatic music vocalist duo as well as playback singers in films in the 1940s and 1950s, before they became music teachers.  The person who does the playback singing is Jayalakshmi but was named as Radha Jayalakshmi in the cine field.  Actually, Radha was her cousin and singing partner on the stage performances.  They were early singers in the trend of duo singing in Carnatic music, which started in the 1950s, with performers like Soolamangalam Sisters, and later continued by Bombay Sisters, Ranjani-Gayatri and Priya Sisters.

N. Viswanathan: N.Viswanathan (1929 – 17 November 2010), popularly known as Calcutta Viswanathan in the Tamil film industry, was an Indian actor and academic.  A Tamilian by birth, he moved to Calcutta (now Kolkata) at a young age and taught English at St. Xavier's College, Calcutta for more than 40 years.  Viswanathan was also a well-known public speaker.  He made his acting debut in Mrinal Sen's "Punascha" and continued to act in Bengali films.  In a career that spanned 40 years, Viswanathan appeared in nearly 100 films in Bengali, Tamil and English.  He was a member several theatre groups and also formed the "Calcutta Players", an acting troupe.

Radha Viswanathan: Radha Viswanathan (born 1934) is an Indian vocalist and former classical dancer.  She has performed extensively with her mother, Bharat Ratna Carnatic vocalist M. S. Subbulakshmi.

Thavapudhalavan: Thavapudhalavan is a 1972 Indian Tamil film, directed by Muktha Srinivasan and produced by V. Ramasami.  The film stars Sivaji Ganesan, K. R. Vijaya, Pandari Bai and Cho in lead roles.  The film had musical score by M. S. Viswanathan.  This film had M.R.Radha and M.R.Vasu shooting scenes together.  M.R.Radha made guest appearance in this film.

Chandan Ka Palna: Chandan Ka Palna is a 1967 Bollywood film starring Dharmendra and Meena Kumari.  No joy in the world can equal the happiness a man derives from watching his own child at play.  Not all the riches in the world can compensate for the vacuum, the emptiness, created by the want of a child in a home.  With a woman this yearning is a hundred times stronger and the outcome of her torment impossible beyond measure.  Radha belonged to a rich family.  Her sole aim in life after becoming a widow, was to see her sone Ajit happy and fulfil the promise she had given to her husband that the family name and tradition would be perpetuated.  Finding Ajit deeply in love with Shobha, the Raisaheb's daughter who too loved him no less, Radha got them married, hoping that Shobha would prove an ideal wife and daughter-in-law and their home would soon resound with merry laughter of a child, if not children.  Three years went by and Radha was still waiting for the new arrival in the family.  Her patience was running out.  Desperate, she took Shobha to a doctor who, after prolonged examination and treatment, told her that God alone could help her fulfill her yearning for a grandchild.  Radha's sorrow knows no bounds.  She could not think of the family chain breaking off.  She had to have a grandchild and fulfil her promise to her late husband.  As a last resort, she took Shobha to Gurudev, the spiritual soul revered by the family.  Gurudev had pity on Radha's plight.  Taking her into confidence, he told her: ""Look, I am no miracle worker.  And, as far as my knowledge goes, I am certain that your daughter-in-law is destined to remain barren." "When Shobha heard this, she was in a daze.  She knew her mother-in-law's craving for a grandchild and she knew also that woman would leave no stone unturned to accomplish her objective.Life seemed to Shobha without a ray of hope for her to live.  She decided to put an end to it.  It was better that way, she thought, than to suffer the humiliation of being branded for ever barren.  She knew how deeply her husband loved her and she could very well imagine his dilemma when forced to marry again for the sake of a child.She started walking in the direction of the fatal plunge to end all problems, to end herself.  But what mere mortal can meet his or her end according to his or her own design?  Destiny had other things written down for Shobha.  But let that be unfolded on the screen in ""Chandan Ka Palna"" lest further knowledge of the proceedings spoil full enjoyment of the drama.

S. Aishwarya: S.Aishwarya born on 27 October in Chennai, Tamil Nadu) is an Indian singer of traditional Carnatic music.  She is the great-granddaughter of M.S. Subbulakshmi.  and the grand daughter of Radha Viswanathan

Viswanathan–Ramamoorthy: Viswanathan–Ramamoorthy were an Indian music-director duo composed of M. S. Viswanathan and T. K. Ramamoorthy.  They worked together on over 100 films, from 1952's "Panam" to 1965's "Aayirathil Oruvan".  After their split, Ramamoorthy worked on 16 films between 1966 and 1986.  He and Viswanathan reunited in 1995 for "Engirundho Vandhan".

Attack (2016 film): Guru Raj (Prakash Raj) the man of the masses, a powerful business man of Charminar Group of Companies who runs his own gang as a mafia don.  He has 3 sons elder one Kaali (Jagapathi Babu), second one Gopi (Vadde Naveen) and the last one is Radha Krishna / Radha (Manchu Manoj).  All his 3 sons are his backbone.  Valli (Surbhi) who loves Radha tries to drag him away from these issues.  Guru Raj was brutally killed by some unknown gangsters while visiting a temple, his family is completely upset this incident and makes them clueless about the motive behind this attack.  Kaali decides to take revenge against the real culprits behind his father’s death.  He starts digging out the possible reasons and motive for this attack and people involved and planned.  Everyone starts going opposite them.  Unfortunately, Kaali is also killed in unusual circumstances.  After these incidents, Radha decides to take revenge on the people behind these attacks and responsible for his father and elder brother’s death.  Finally, he solve the murders & takes revenge.

Souten Ki Beti: Heart Specialist Dr. Shyam Verma is the only child of his widowed father, Shankar.  Shyam who is a complete casanova wooes a beautiful Air Hostess, Radha.  One fine day Shyam and Radha get intimate under the inducement of alcohol.  Radha gets pregnant but Shyam weds his father's friends Jagannath's daughter, Rukmini.  Heartbroken Radha quits her job and re locates to Kashmir where she gives birth to Dipinti.  Years later Shyam and Radha meet again while Rukmini finds out about their strong affair.  Rukmani gets them to reconcile and marry.  Years later when Dipinti turns 16 years old, she falls in love with rich lad Amit Mehra.  Amit's dad, Advocate Mehra, who refuses to permit his 20-year-old son to marry the daughter of a mistress, and a woman born out of wedlock.  Will Amit go against his fathers wish and marry his love Dipinti?

Question: What ethnicity are both S. Aishwarya and Radha Viswanathan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "shared_ethnicity": {
      "type": "string",
      "description": "The common ethnicity of the individuals mentioned."
    },
    "individuals": {
      "type": "array",
      "description": "List of individuals whose ethnicity is being identified.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "primary_role": {
            "type": "string",
            "description": "The primary role or profession of the individual as described in the context."
          }
        },
        "required": [
          "name",
          "primary_role"
        ],
        "additionalProperties": false
      }
    },
    "number_of_individuals": {
      "type": "integer",
      "description": "The total number of individuals whose ethnicity is being identified."
    }
  },
  "required": [
    "shared_ethnicity",
    "individuals",
    "number_of_individuals"
  ],
  "additionalProperties": false
}
