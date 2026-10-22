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
Goal of the Month (Germany): The Goal of the Month (German: "Tor des Monats" ) is, like the "Goal of the Year", the "ARD Goal of the Decade" and "Goal of the Century", an individual soccer award selected by viewers of "Sportschau" (German TV channel ARD).  Honored are spectatular or important football goals mostly scored in or for Germany.

Goparaju Ramachandra Rao: Goparaju Ramachandra Rao (nickname: Gora) (15 November 1902 – 26 July 1975) was an Indian social reformer, atheist activist and a participant in the Indian independence movement.  He authored many books on atheism and proposed atheism as self-confidence.  He propagated positive atheism by his articles, speeches, books and his social work.  He is the founder of Atheist Centre along with his wife Saraswathi Gora and a few volunteers.

Nooksack Salmon Enhancement Association: Nooksack Salmon Enhancement Association (NSEA) was formed in 1990 as a non-profit organization with an overall goal of seeing an increase in returning natural spawning salmon to the over 1,600 km of rivers and streams in Whatcom County, Washington in the United States.  The association was formed as part of Washington State's Regional Fisheries Enhancement Groups Program established by the Washington State Legislature in 1990 to involve local communities, citizen volunteers, and landowners in the state’s salmon recovery efforts.  NSEA is one of 14 groups in Washington State each with the common goal of restoring salmonid populations and habitat within their region.

Intelligent design movement: The intelligent design movement is a neo-creationist religious campaign for broad social, academic and political change to promote and support the pseudoscientific idea of intelligent design (ID), which asserts that "certain features of the universe and of living things are best explained by an intelligent cause, not an undirected process such as natural selection."  Its chief activities are a campaign to promote public awareness of this concept, the lobbying of policymakers to include its teaching in high school science classes, and legal action, either to defend such teaching or to remove barriers otherwise preventing it.  The movement arose out of the previous Christian fundamentalist and evangelistic creation science movement in the United States, and is driven by a small group of proponents.  The overall goal of the intelligent design movement is to overthrow materialism and atheism.  Its proponents believe that society has suffered "devastating" cultural consequences from adopting materialism and that science is the cause of the decay into materialism because it seeks only natural explanations, and is therefore atheistic.  They believe that the scientific theory of evolution implies that humans have no spiritual nature, no moral purpose, and no intrinsic meaning.  They seek to "reverse the stifling dominance of the materialist worldview" represented by the theory of evolution in favor of "a science consonant with Christian and theistic convictions."

Development-supported agriculture: Development-supported agriculture (DSA) is a nascent movement in real estate development that preserves and invests in agricultural land use.  As farmland is lost due to the challenging economics of farming and the pressures of the real estate industry, DSA attempts to reconcile the need for development with the need to preserve agricultural land.  The overall goal of DSA is to incubate small-scale organic farms that co-exist with residential land development, providing benefits to farmers, residents, the local community, and the environment.

Mirza Fatali Akhundov: Mirza Fatali Akhundzade (Azerbaijani: "Mirzə Fətəli Axundov" میرزا فتحعلی آخوندزاده) or Mirza Fath-Ali Akhundzade (Persian: میرزا فتحعلی آخوندزاده‎ ‎ ), also known as Akhundov (12 July 1812 – 9 March 1878), was a celebrated ethnic Azerbaijani author, playwright, philosopher, and founder of modern literary criticism, "who acquired fame primarily as the writer of European-inspired plays in the Azeri Turkic language".  Akhundzade singlehandedly opened a new stage of development of Azerbaijani literature.  He was also the founder of materialism and atheism movement in Azerbaijan and one of forerunners of modern Iranian nationalism.

Kurt Meyer (footballer): Kurt Meyer (4 February 1921 – 23 August 2008), nicknamed "Meyer 15" or respectfully "Fußballopa" (Soccer Grandpa), was a German amateur soccer player for "Blau-Weiß Post Recklinghausen".  He achieved nationwide fame when he scored the German "ARD Goal of the Month" and later the "ARD Goal of the Year" in 2001 at age 80.  He is by far the oldest player to have won any of these awards.

Ard Louis: Ard A. Louis is a Professor of Theoretical Physics at the University of Oxford, where he leads an interdisciplinary research group studying problems on the border between chemistry, physics and biology, and is also director of graduate studies in theoretical physics.  From 2002 to 2010 he was a Royal Society University Research Fellow at the University of Cambridge and the University of Oxford.  He is also an associate of the Faraday Institute for Science and Religion.  He has written for the BioLogos Foundation, where as of November 2011, he sat on the Board of Directors.  He has been criticised by the Discovery Institute for his opposition to the Intelligent design movement.  In 2013 he was elected a member of the International Society for Science and Religion.  He engages in molecular gastronomy.

Irreligion in India: Atheism and agnosticism have a long history in India and flourished within the Sramana movement.  Indian religions like Jainism, Buddhism and some schools of Hinduism consider atheism to be acceptable.  India has produced some notable atheist politicians and social reformers.  According to 2011 Census of India, 99.76% of Indians are religious while 0.24% did not state their religious identity.  According to the 2012 WIN-Gallup Global Index of Religion and Atheism report, 81% of Indians were religious, 13% were not religious, 3% were convinced atheists, and 3% were unsure or did not respond.

Michael Stahl: Michael Stahl (born 15 September 1987 in Diez) is a German football player with TuS Koblenz.  His position is midfield.  On 26 October 2010, he scored a 61-meter goal in a DFB-Pokal match against Hertha BSC.  Koblenz continued to win the match 2-1, and the goal was voted as the ARD Goal of the Month and as the Goal of the Year.

Question: The overall goal of this movement is to overthrow materialism and atheism and is opposed by Ard A. Louis?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movement_name": {
      "type": "string",
      "description": "The name of the movement."
    },
    "movement_overall_goal": {
      "type": "string",
      "description": "The stated overall goal of the movement."
    },
    "opposing_individual": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual who opposes the movement."
        },
        "reason_for_opposition_mention": {
          "type": "string",
          "description": "A phrase from the text indicating the individual's opposition to the movement."
        }
      },
      "required": [
        "name",
        "reason_for_opposition_mention"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movement_name",
    "movement_overall_goal",
    "opposing_individual"
  ],
  "additionalProperties": false
}
