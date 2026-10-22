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
Keli Lane: Keli Lane (born 21 March 1975), a former Australian water polo player, was convicted of the 1996 murder of her newborn baby Tegan, and three counts of lying under oath.  Lane is currently serving an 18-year prison sentence and will be eligible for parole on 12 May 2023, after serving a period of 13 years and five months in custody.  On 18 April 2011, Lane's lawyers lodged an appeal against her conviction at the same time as a Sydney taxi driver made claim he allegedly saw Lane dispose of the child.  Her final application for appeal was rejected by the High Court in August 2014.

Victoire Ingabire Umuhoza: Victoire Ingabire Umuhoza (born 3 October 1968) is the chairperson of the Unified Democratic Forces (UDF), a coalition of Rwandan exile opposition groups with a large base of active members in Rwanda, Europe, United States of America and in Canada.  She was a party candidate for Rwanda's August 2010 elections, but was ultimately arrested and sentenced to prison.  A Sakharov Prize nominee, she is currently serving a 15-year prison sentence in Kigali Central Prison on charges of terrorism and threatening national security.

Jack Reeves: Jack Wayne Reeves was born in 1940.  He is currently serving a lengthy prison sentence for murdering his second and fourth wife.

David Strecker: David Strecker (born August 12, 1950) also known by the alias Cuba Dave, is a retired American laborer currently serving a 5-year prison sentence in Costa Rica for the promotion of sex tourism.  Prior to his arrest and conviction, Strecker was held in preventative detention in San Sebastián prison in San José, Costa Rica.  He is the first individual to be targeted for prosecution under Costa Rica's controversial new law, passed in 2012, that makes it illegal for a third party to profit on prostitution.

Trial of Oscar Pistorius: The trial of Oscar Pistorius for the murder of Reeva Steenkamp and several gun-related charges (The State vs Oscar Pistorius) in the High Court of South Africa in Pretoria opened on 3 March 2014.  On 11–12 September 2014, Judge Thokozile Masipa delivered a verdict that Pistorius was not guilty of murder, but guilty of the culpable homicide of Steenkamp and reckless endangerment with a firearm at a restaurant.  On 21 October 2014, Pistorius received a prison sentence of a maximum of five years for culpable homicide and a concurrent three-year suspended prison sentence for the separate reckless endangerment conviction.

Jeff Fort: Jeff Fort (born February 20, 1947; also known as Abdul Malik Ka'bah) is an American former gang leader from Chicago, Illinois.  Fort is the co-founder of the Black P. Stones gang and founder of its El Rukn faction.  Fort is currently serving a total of 155 year prison sentence; 80 year prison sentence after being convicted of conspiracy and weapons charges in 1987 for plotting to commit attacks inside the U.S. in exchange for weapons and $2.5 million from Libya and a 75 year sentence for ordering a murder in 1981.  Fort was also convicted of drug trafficking in 1983 and sentenced to 13 years in prison.

R v Latimer: R v Latimer [2001] 1 S.C.R. 3, was a decision by the Supreme Court of Canada in the controversial case of Robert Latimer, a Saskatchewan farmer convicted of murdering his disabled daughter Tracy Latimer.  The case had sparked an intense national debate as to the ethics of what was claimed as a mercy killing.  In its decision, the Supreme Court ruled that the crime could not be justified through the defence of necessity, and found that, despite the special circumstances of the case, the lengthy prison sentence given to Latimer was not cruel and unusual and therefore not a breach of section 12 of the Canadian Charter of Rights and Freedoms.  The Court also ruled that Latimer was not denied rights to jury nullification, as no such rights exist.  The prison sentence was thus upheld, although the Court specifically noted that the federal government had the power to pardon him.

Christian Gerhartsreiter: Christian Karl Gerhartsreiter (born February 21, 1961) is a convicted murderer and impostor born in Germany who is currently serving a prison sentence in the United States.  In his late teens, Gerhartsreiter moved to the US where he lived under a succession of aliases while variously claiming to be an actor, director, art collector, a physicist, a ship's captain, a negotiator of international debt agreements, and an English aristocrat.

Jeffrey Skilling: Jeffrey Keith "Jeff" Skilling (born November 25, 1953) is the former CEO of Enron Corporation.  In 2006, he was convicted of federal felony charges relating to Enron's collapse and is currently serving 14 years of a 24-year, four-month prison sentence at the Federal Prison Camp (FPC) – Montgomery in Montgomery, Alabama.  The Supreme Court of the United States heard arguments in the appeal of the case March 1, 2010.  On June 24, 2010, the Supreme Court vacated part of Skilling's conviction and transferred the case back to the lower court for resentencing.  During April 2011, a three-judge 5th Circuit Court of Appeals panel ruled that the verdict would have been the same despite the legal issues being discussed, and Skilling's conviction was confirmed; however, the court ruled Skilling should be resentenced.  Skilling appealed this new decision to the Supreme Court, but the appeal was denied.  In 2013, the United States Department of Justice reached a deal with Skilling, which resulted in ten years being cut from his sentence.

Who Is Clark Rockefeller?: Who Is Clark Rockefeller?  is a 2010 American police procedural television film directed by Mikael Salomon and written and co-produced by Edithe Swensen.  It stars Eric McCormack as Christian Gerhartsreiter/Clark Rockefeller and Sherry Stringfield as Sandra Boss.  The film is based on the life of Christian Gerhartsreiter, a German con artist who for years impersonated many people, at one point claiming to be part of the Rockefeller family going by the faux name "Clark Rockefeller", and kidnapping his daughter.  Filming took place in Toronto in October 2009 and was released on March 13, 2010 on the Lifetime network to mixed reviews.

Question: Where did Karl Gerhartsreiter move to in his teens and is currently serving a prison sentence?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "country_moved_to_in_teens": {
      "type": "string",
      "description": "The country the person moved to in their late teens."
    },
    "country_serving_sentence": {
      "type": "string",
      "description": "The country where the person is currently serving a prison sentence."
    },
    "crimes_committed": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of crimes the person was convicted of."
    }
  },
  "required": [
    "person_name",
    "country_moved_to_in_teens",
    "country_serving_sentence",
    "crimes_committed"
  ],
  "additionalProperties": false
}
