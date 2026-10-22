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
Park Dietz: Park Dietz (born 1948) is a forensic psychiatrist who has consulted or testified in many of the highest profile US criminal cases including Joel Rifkin, Arthur Shawcross, Jeffrey Dahmer, The Unabomber, Richard Kuklinski, the Beltway sniper attacks, and Jared Lee Loughner.

Clinical vampirism: Clinical vampirism, more commonly called Renfield's syndrome or Renfield syndrome, is an obsession with drinking blood.  The earliest formal presentation of clinical vampirism to appear in the psychiatric literature, with the psychoanalytic interpretation of two cases, was contributed by Richard L. Vanden Bergh and John F. Kelley in 1964.  As the authors point out, brief and sporadic reports of blood-drinking behaviors associated with sexual pleasure have appeared in the psychiatric literature at least since 1892 with the work of Austrian forensic psychiatrist Richard von Krafft-Ebing.  Many medical publications concerning clinical vampirism can be found in the literature of forensic psychiatry, with the unusual behavior reported as one of many aspects of extraordinary violent crimes.  The behavior has never gained official recognition by the psychiatric profession and is not found in any edition of the "International Classification of Diseases" or the "Diagnostic and Statistical Manual of Mental Disorders".  However, in the more colorful era in the history of psychiatry that predated the 1980s rise of the coded categories of (supposedly) theory-neutral mental disorders in "DSM" and "ICD", the psychiatric literature was fertile ground for the flourishing of case history reports of "uncommon psychiatric syndromes" or "extraordinary disorders of human behavior" that included not only clinical vampirism, but also lycanthropy, possession, stigmata and other unusual phenomena.

Criminal Case (video game): Criminal Case (commonly abbreviated as "CC") is a detective-themed hidden object game released on November 15, 2012 for Facebook.  An iOS version was released worldwide on August 28, 2014, followed by an Android version on April 15, 2015.  Developed and published by French indie studio Pretty Simple, "Criminal Case" has over ten million average monthly users.  "Criminal Case" has become a very popular game since the start of 2013 and also has been highly competitive with "Candy Crush Saga", the most popular game on Facebook with over 46 million average monthly users.  On December 9, 2013, "Criminal Case" was crowned the Facebook Game of the Year 2013, surpassing "Candy Crush".

Manfred Guttmacher: Manfred Schanfarten Guttmacher (May 19, 1898 – November 7, 1966) was an American forensic psychiatrist and chief medical officer noted for his connection of psychiatry and criminal law.  Among several notable cases, Guttmacher testified in the trial of Jack Ruby, and authored "The Dog Must Wag The Tail: Psychiatry And The Law", "America's Last King: An Interpretation of the Madness of George III" and other works.

Wolfram Meier-Augenstein: Wolfram Meier-Augenstein is a Professor at Robert Gordon University, Aberdeen, a registered forensic expert advisor with the British National Crime Agency and a member of the Advisory Board of the journal "Rapid Communications in Mass Spectrometry".  From 2010 to 2014 he served as Director of the Forensic Isotope Ratio Mass Spectrometry Network (FIRMS).  while from 2009 to 2013 he was a Council member of the British Association for Human Identification (BAHID).  Meier-Augenstein was one of the scientists consulted by An Garda Síochána investigating the case of the dismembered torso found in the Dublin Royal Canal.  This case has gained some notoriety under the name Scissor Sisters (convicted killers).  He was also one of the scientists consulted by the police investigating the Norfolk headless body case.

J. Anderson Thomson: J. Anderson Thomson, Jr. is an American psychiatrist and writer.  He is a Trustee of the Richard Dawkins Foundation for Reason and Science and a staff psychiatrist for Counseling and Psychological Services at the University of Virginia Student Health Center, as well as the University of Virginia's Institute for Law, Psychiatry and Public Policy.  Thomson also has his own private practice, and is a forensic psychiatrist for Region Ten Community Services.  Thomson acquired his B.A. from Duke University in 1970, he acquired his M.D. from the University of Virginia in 1974, and he did his adult psychiatry training at the University of Virginia from 1974 to 1977.

Richard Kuklinski: Richard Leonard Kuklinski (April 11, 1935 – March 5, 2006) was an American contract killer and serial killer who was convicted of murdering five people, though he likely killed at least several dozen more.  He was associated with members of the American Mafia, namely the DeCavalcante crime family of Newark, New Jersey, and the Five Families of New York City.

Michael Welner: Michael Mark Welner, M.D., (born September 24, 1964, in Pittsburgh, Pennsylvania) is an American forensic psychiatrist and Chairman of The Forensic Panel.  Welner is best known for his work in sensitive and complex litigation.  He has acted as lead forensic psychiatric examiner in numerous criminal or court proceedings of national and international prominence, including precedent-setting trials and higher court decisions.  Welner is also known for a number of innovations in forensic science, forensic psychiatry and justice, including protocols for prospective peer review in forensic medicine consultation, research to standardize an evidence-based distinction of the worst crimes, The Depravity Standard, and recommendations for upgrading forensic science assessment.  He has been featured in network television news coverage of forensic psychiatry issues, has authored publications for professional and public audiences, and has contributed to emerging legislation on mental health reform.

David Corwin: David L. Corwin is a board-certified psychiatrist, child and adolescent psychiatrist, and forensic psychiatrist.  Corwin has done extensive work into the long-term impact of child violence and abuse on health, and has promoted family support and treatment programs.  Corwin has worked as a consultant, a lecturer, a trainer, and an evaluator of suspected or known child sexual abuse cases throughout many countries, as well as serving as an expert witness of child sexual abuse cases.  Corwin has founded, directed or chaired groups that serve to advance prevention and protection against child violence and abuse, as well as furthering the education and research of the impact of child abuse.

James Grigson: James Grigson (January 30, 1932 – June 3, 2004), nicknamed "Doctor Death" by some press accounts, was a Texas forensic psychiatrist who testified in 167 capital trials, nearly all of which resulted in death sentences.  He was exposed as a charlatan and expelled by the American Psychiatric Association and the Texas Society of Psychiatric Physicians in 1995 for unethical conduct.

Question:  Park Dietz is a forensic psychiatrist who consulted or testified in the criminal case of an American contract killer who was associated with members of what Newark family?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "forensic_psychiatrist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the forensic psychiatrist"
        },
        "role_in_case": {
          "type": "string",
          "description": "The role of the psychiatrist in the criminal case (e.g., consulted, testified)"
        }
      },
      "required": [
        "name",
        "role_in_case"
      ],
      "additionalProperties": false
    },
    "criminal_case_subject": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual involved in the criminal case"
        },
        "occupation_type": {
          "type": "string",
          "description": "The occupation or type of criminal the subject was"
        }
      },
      "required": [
        "name",
        "occupation_type"
      ],
      "additionalProperties": false
    },
    "associated_crime_families": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "family_name": {
            "type": "string",
            "description": "The name of the crime family"
          },
          "location": {
            "type": "string",
            "description": "The primary location associated with the crime family"
          }
        },
        "required": [
          "family_name",
          "location"
        ],
        "additionalProperties": false
      },
      "description": "A list of crime families the subject was associated with"
    },
    "newark_associated_family_name": {
      "type": "string",
      "description": "The name of the crime family specifically associated with Newark"
    }
  },
  "required": [
    "forensic_psychiatrist",
    "criminal_case_subject",
    "associated_crime_families",
    "newark_associated_family_name"
  ],
  "additionalProperties": false
}
