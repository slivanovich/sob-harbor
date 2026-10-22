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
Life imprisonment in Ireland: A Life sentence in Ireland may last for the natural life of the convict.  It is not necessarily "life imprisonment" in practice, as not all of the life sentence is generally served in prison custody.  The granting of temporary or early release of life sentenced prisoners is a feature of the Irish prison system handled by the Minister for Justice and Equality.

Federal Correctional Institution, Terre Haute: The Federal Correctional Institution, Terre Haute (FCI Terre Haute) is a medium-security United States federal prison for male inmates in Indiana.  It is part of the Terre Haute Federal Correctional Complex (FCC Terre Haute) and is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  The facility also has an adjacent satellite prison camp for minimum-security male offenders.

Tyrone Werts: Tyrone Werts is an American man who was convicted of a second-degree murder committed in 1975, for which he received a life sentence; however, he was released after 36 years instead.  This was an extremely rare case as the law in Pennsylvania says that if you have been charged with 1st or 2nd degree murder and were given a life sentence, there is no possibility for parole (Gottschalk).  He is most known as an ex-convict who was released from Prison after serving 36 years of what was supposed to be a life sentence.  While serving his time at Graterford Prison, in Perkiomen, Pennsylvania, Werts served as the president of the “Lifers” and made many very influential and positive changes in the prison community.

Life imprisonment in the United States: In the United States, 1 in every 2,000 residents is imprisoned for life.  This is similar to the total imprisonment rate in Japan, which is roughly 51 per 100,000 residents.  There are many U.S. states where a convict can be released on parole after a decade or more has passed.  For example, sentences of "15 years to life", "25 years to life", or "life with mercy" may be given; this is called an "indeterminate life sentence", while a sentence of "life without the possibility of parole" or "life without mercy" is called a "determinate life sentence".  Even when a sentence specifically denies the possibility of parole, government officials may have the power to grant amnesty or reprieves, or commute a sentence to time served.

Alvin and Judith Neelley: Alvin Howard Neelley, Jr. (1953–2005) and Judith Ann Adams Neelley (born 1964) are an American couple who committed two torture murders.  They each were convicted of the kidnappings and murders of Lisa Ann Millican and Janice Kay Chatman and attempted to commit a third.  Judith Neelley was sentenced to death by the State of Alabama (1983), but her sentence was commuted to life imprisonment (1999).  She is serving her sentence at the Julia Tutwiler Prison for Women in Wetumpka, Alabama.  Alvin Neelley was serving a life sentence at the Bostick State Prison in Hardwick, Georgia at the time of his death in 2005.

Hiroshi Nakamura (dissident): Hiroshi Nakamura (中村 泰 , Nakamura Hiroshi , born 1930) is a Japanese dissident.  After the Korean War broke out, he dropped out of Tokyo University, and decided to fight against Japan.  He was multilingual and became a good shot by training.  On November 23, 1956, he shot a policeman to death and received a life sentence.  He was paroled in 1976.  Following his release, he attempted to found an armed organization and collected guns.  After being arrested for an attempted robbery in 2002, he was sentenced to 15 years in prison for the crime and also received another life sentence for his previous 2001 injury case.  He was also suspected of the 1995 shooting of Takaji Kunimatsu, who was a chief of the National Police Agency.

Life Sentence (TV series): Life Sentence (stylized as l;fe sentence) is an American comedy-drama series that will debut on The CW as a midseason entry during the 2017–18 television season that was created by Erin Cardillo & Richard Keith, who will executive produce with Oliver Goldstick, Bill Lawrence, Jeff Ingold, and director Lee Toland Krieger.  The show is produced by In Good Company, Doozer Productions and Warner Bros.  Television.  The CW officially ordered "Life Sentence" to series on May 10, 2017.  In August 2017, star Lucy Hale revealed that the series is set to premiere in January 2018.

Mohammed Abdul Qadeer: Abdul Qadeer was the ex-constable of police from Hyderabad, who was convicted for life sentence for killing ACP Sattiah, who was illegally harassing Muslim youth during the Babri Masjid demolition riots in 1992.  Abdul qadeer was illegally detained in jail despite the completion period of his life imprisonment.  Many muslim organizations appealed for the release of Mohammed abdul qadeer on the grounds of his health but previous governments declined the plea.  He was finally released from jail by the Government of Telangana on 29 March 2016. He Passed Away On The Night Of 14 September 2017 In His Hometown Hyderabad,India.  Former Supreme Court judge Markandey Katju sought the release of ex-constable mohammed Abdul qadeer who is serving a life sentence at Cherlapalli jail, on humanitarian grounds.  Katju twitted on social media K Chandrasekhar Rao for the release of ex-constable on humanitarian grounds.

John K. Giles: John Knight Giles (February 16, 1895February 8, 1979) was an inmate at Alcatraz prison, most well known for an escape attempt in 1945.  He was originally sentenced to the United States Penitentiary on May 11, 1935 for attempted robbery of the Denver and Rio Grande Western mail train; he had previously been serving a life sentence in Oregon for murder before escaping.  Giles began serving his federal sentence for the attempted train robbery at McNeil Island on June 17, 1935, but due to his escape record and the length of his sentence, was transferred to Alcatraz Island on August 28, 1935.

Aldrich Ames: Aldrich Hazen Ames (born May 26, 1941) is a former Central Intelligence Agency (CIA) officer turned KGB mole, who was convicted of espionage in 1994.  He is serving a life sentence without the possibility of parole in the Federal Correctional Institution in Terre Haute, Indiana, United States.  Ames was formerly a 31-year CIA counterintelligence analyst who committed espionage against the U.S. by spying for the Soviet Union and Russia.  At the time of his arrest, Ames had compromised more CIA assets than any other mole in history until Robert Hanssen's arrest seven years later.

Question: What is the name of the complex where Aldrich Hazen Ames is serving a life sentence?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "prisoner_name": {
      "type": "string",
      "description": "The name of the prisoner."
    },
    "prison_institution": {
      "type": "string",
      "description": "The specific correctional institution where the prisoner is serving their sentence."
    },
    "prison_complex": {
      "type": "string",
      "description": "The larger correctional complex that the institution is part of."
    },
    "sentence_details": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of sentence received."
        },
        "parole_possibility": {
          "type": "boolean",
          "description": "Indicates if parole is possible for this sentence."
        }
      },
      "required": [
        "type",
        "parole_possibility"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "prisoner_name",
    "prison_institution",
    "prison_complex",
    "sentence_details"
  ],
  "additionalProperties": false
}
