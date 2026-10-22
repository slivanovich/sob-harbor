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
Daniel Elliott Huger: Daniel Elliott Huger (June 28, 1779August 21, 1854) was a United States Senator from South Carolina.  Born on Limerick plantation, Berkeley County (near Charleston), his father was Daniel Huger, a Continental Congressman and U.S. Representative from South Carolina.  Daniel Elliott pursued classical studies in Charleston and graduated from the College of New Jersey (later Princeton University) in 1798.  He studied law and was admitted to the bar in 1799, beginning practice in Charleston.  In 1800 he married Isabella Johannes Middleton-daughter of Declaration of Independence signer Arthur Middleton.  He was a member of the South Carolina House of Representatives from 1804 to 1819 and from 1830 to 1832, and was a brigadier general of State troops in 1814.  He was judge of the circuit court from 1819 to 1830, and was a member of the South Carolina State Senate from 1838 to 1842.  He was an opposition member of the State nullification convention in 1832.

Benjamin Huger (American Revolution): Benjamin Huger (1746 – 11 May 1779) was one of five Huger brothers from South Carolina who served in the American Revolutionary War.  Huger became a close friend of La Fayette, having met him upon his arrival near Georgetown in 1777, and his son Francis Kinloch Huger had a role in getting La Fayette temporarily released from prison at Olomouc in the 1790s.

Gilbert du Motier, Marquis de Lafayette: Marie-Joseph Paul Yves Roch Gilbert du Motier, Marquis de Lafayette (] ; 6 September 1757 – 20 May 1834), in the United States often known simply as Lafayette, was a French aristocrat and military officer who fought in the American Revolutionary War.  A close friend of George Washington, Alexander Hamilton, and Thomas Jefferson, Lafayette was a key figure in the French Revolution of 1789 and the July Revolution of 1830.

Implied powers: Implied powers, in the United States, are those powers authorized by the Constitution that, while not stated, seem to be implied by powers expressly stated.  When George Washington asked Alexander Hamilton to defend the constitutionality of the First Bank of the United States against the protests of Thomas Jefferson, James Madison, and Attorney General Edmund Randolph, Hamilton produced what has now become the classic statement for implied powers.  Hamilton argued that the sovereign duties of a government implied the right to use means adequate to its ends.  Although the United States government was sovereign only as to certain objects, it was impossible to define all the means which it should use, because it was impossible for the founders to anticipate all future exigencies.  Hamilton noted that the "general welfare clause" and the "necessary and proper clause" gave elasticity to the constitution.  Hamilton won the argument with Washington, who signed his Bank Bill into law.

Anti-Administration party: The "Anti-Administration party" (1789–1792) was an informal faction led by James Madison and Thomas Jefferson that opposed policies of then United States Secretary of the Treasury, Alexander Hamilton in the first term (1789–1792) of President George Washington.  This was not an organized political party, but an unorganized faction.  Most had been Anti-Federalists in 1788, meaning they opposed ratification of the Constitution of the United States.  However, the situation was fluid, with members moving in and out.

Francis Kinloch Huger: Colonel Dr. Francis Kinloch Huger (September 17, 1773 – February 14, 1855), a trained physician and artillery officer, was a scion of the Huger family of South Carolina.  A member of the South Carolina House of Representatives and South Carolina Senate, he is best known for his leadership of a failed November 1794 attempt to rescue Lafayette from captivity during the wars surrounding the French Revolution.

Enoch Edwards (surgeon): Enoch Edwards (1751 – April 18, 1802, Frankford, Philadelphia, Pennsylvania) was an American physician and a leading Patriot during the American Revolution.  Born in Lower Dublin Township, Pennsylvania, Edwards was a member of the Provincial Congress in Carpenters' Hall on June 18, 1776, which led to the Pennsylvania Constitution of 1776.  He was also a signatory of the 1790 Pennsylvania Constitution.  During the war he served as attending physician for George Washington, was a close friend of both Benjamin Rush and Thomas Jefferson, and kept up correspondence with James Monroe and John Quincy Adams.

Alexander Hamilton: Alexander Hamilton (January 11, 1755 or 1757July 12, 1804) was an American statesman and one of the Founding Fathers of the United States.  He was an influential interpreter and promoter of the U.S. Constitution, as well as the founder of the nation's financial system, the Federalist Party, the United States Coast Guard, and "The New York Post" newspaper.  As the first Secretary of the Treasury, Hamilton was the main author of the economic policies of the George Washington administration.  He took the lead in the funding of the states' debts by the Federal government, as well as the establishment of a national bank, a system of tariffs, and friendly trade relations with Britain.  His vision included a strong central government led by a vigorous executive branch, a strong commercial economy, with a national bank and support for manufacturing, plus a strong military.  This was challenged by Virginia agrarians Thomas Jefferson and James Madison, who formed a rival party, the Democratic-Republican Party.  They favored strong states based in rural America and protected by state militias as opposed to a strong national army and navy.  They denounced Hamilton as too friendly toward Britain and toward monarchy in general, and too oriented toward cities, business and banking.

Democratic-Republican Party: The Democratic-Republican Party was an American political party formed by Thomas Jefferson and James Madison in 1791–93 to oppose the centralizing policies of the new Federalist Party run by Alexander Hamilton (1755/57-1804), who was secretary of the treasury and chief architect of George Washington's administration.  The new party controlled the presidency and Congress, as well as most states, from 1801 to 1825, during the First Party System.  It began in 1791 as one faction in Congress, and included many politicians who had been opposed to the new constitution.  They called themselves "Republicans" after their ideology, Republicanism.  They distrusted the Federalist commitment to republicanism.  The party splintered in 1824 into the Jacksonian movement (which became the Democratic Party in 1828) and the short-lived National Republican Party (later succeeded by the Whig Party).

Thomas Jefferson (Cleveland): Thomas Jefferson is a bronze statue of Thomas Jefferson flanking the steps leading into the Cuyahoga County Courthouse in Cleveland, Ohio.  It is one of four statues Bitter created for the project, there was another bronze Alexander Hamilton and two marble attic figures, John Somers and Lord Mansfield.  Jefferson is portrayed wearing 18th Century clothes, sitting in a klismos chair holding “papers of state in hand.”  “It is a youthful and rebellious Jefferson, author of the Declaration of Independence who appears before us in Cleveland.”  This Jefferson is portrayed in a “generally rustic appearance” as opposed to the nearby Hamilton who is seen as an “aggressive young aristocrat.”

Question: Which close friend of George Washington, Alexander Hamilton, and Thomas Jefferson, did a scion of the Huger family of South Carolina attempt to rescue?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rescued_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person who was the target of the rescue attempt."
        },
        "description": {
          "type": "string",
          "description": "A brief description of the rescued person's background or role."
        },
        "close_friends": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of individuals identified as close friends of the rescued person."
        }
      },
      "required": [
        "name",
        "description",
        "close_friends"
      ],
      "additionalProperties": false
    },
    "rescuer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the individual who led the rescue attempt."
        },
        "family_name": {
          "type": "string",
          "description": "The family name of the rescuer."
        },
        "rescue_attempt_details": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "The year the rescue attempt took place."
            },
            "outcome": {
              "type": "string",
              "description": "The outcome of the rescue attempt (e.g., 'failed', 'successful')."
            }
          },
          "required": [
            "year",
            "outcome"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "family_name",
        "rescue_attempt_details"
      ],
      "additionalProperties": false
    },
    "question_focus": {
      "type": "string",
      "description": "The primary entity the question is asking to identify."
    }
  },
  "required": [
    "rescued_person",
    "rescuer",
    "question_focus"
  ],
  "additionalProperties": false
}
