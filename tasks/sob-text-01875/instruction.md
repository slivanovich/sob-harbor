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
Commission on Foreign Economic Policy: The U.S. President's Commission on Foreign Economic Policy (the Randall Commission) was established on August 7, 1953 by Public Law 215 entitled "Trade Agreements Extension Act of 1953" which extended the Trade Agreements Extension Act of 1951 for one year.  On April 7, 1953 President Dwight D. Eisenhower requested that Congress extend for one year the Reciprocal Trade Agreements Act, a measure which had originally been passed in 1934.  Under this act and its subsequent extensions, the President was authorized to negotiate agreements with other countries for tariff reduction.  In his message of April 7, the President called for a commission to study U.S. foreign economic policy in general.  Section 301 of this Act provided for a bipartisan commission which consisted of seventeen members: seven appointed by the President, five appointed from the Senate by the Vice President, and five from the United States House of Representatives by the Speaker.  President Eisenhower appointed Clarence B. Randall, Chairman of the Board of Inland Steel Company, as Chairman of the Commission.  The Commission was directed to examine and report on the subjects of international trade, foreign economic policy, and the trade aspects of national security and total foreign policy.  It was to recommend appropriate policies, measures, and practices, based on its findings, in a report to Congress.

Ronald Reagan: Ronald Wilson Reagan ( ; February 6, 1911 – June 5, 2004) was an American statesman and actor who served as the 40th President of the United States from 1981 to 1989.  Before his presidency, he was the 33rd Governor of California, from 1967 to 1975, after a career as a Hollywood actor and union leader.

Algerian presidential election, 2014: Presidential elections were held in Algeria on 17 April 2014.  Incumbent President Abdelaziz Bouteflika was re-elected with 82% of the vote.  Issues in the campaign included a desire for domestic stability after the bloody civil war of the 1990s, the state of the economy (30% unemployment), the frail health of the 15 year incumbent and 77-year-old president whose speech was "slurred and inaudible" in his only public outing during the campaign, and the less-than-wholehearted support given the president by normally united and discrete ruling class.

Foreign policy: A country's foreign policy, also called foreign relations or foreign affairs -policy, consists of self-interest strategies chosen by the state to safeguard its national interests and to achieve goals within its international relations milieu.  The approaches are strategically employed to interact with other countries.  The study of such strategies is called foreign policy analysis.  In recent times, due to the deepening level of globalization and transnational activities, the states will also have to interact with non-state actors.  The aforementioned interaction is evaluated and monitored in attempts to maximize benefits of multilateral international cooperation.  Since the national interests are paramount, foreign policies are designed by the government through high-level decision making processes.  National interests accomplishment can occur as a result of peaceful cooperation with other nations, or through exploitation.  Usually, creating foreign policy is the job of the head of government and the foreign minister (or equivalent).  In some countries the legislature also has considerable effects.  Foreign policies of countries have varying rates of change and scopes of intent, which can be affected by factors that change the perceived national interests or even affect the stability of the country itself.  The foreign policy of one country can have profound and lasting impact on many other countries and on the course of international relations as a whole, such as the Monroe Doctrine conflicting with the mercantilist policies of 19th-century European countries and the goals of independence of newly formed Central American and South American countries.

Policy studies: Policy studies emerged in the United States in the 1960s and 1970s as an subdisicipline of political science.  The study of public policy includes the analysis of both the process of policymaking (the policy process) and the contents of policy (policy analysis).  Policy analysis includes substantive area research (such as health or education policy), program evaluation and impact studies, and policy design.  It "involves systematically studying the nature, causes, and effects of alternative public policies, with particular emphasis on determining the policies that will achieve given goals."

Network for Public Policy Studies: The Network for Public Policy Studies (NPPS) or Shams is an academic peer-reviewed website, under the supervision of Center for Strategic Studies, dedicated to the study of public policies with an emphasis on Iranian Government's policies.  The NPPS publishes articles in Persian and English, covering topics including environmental policy, economic policy, foreign policy, science policy, technology policy, health policy, social policy and cultural policy.  Mohammad Fazeli is the general editor of the website.

United States presidential election, 1828: The United States presidential election of 1828 was the 11th quadrennial presidential election, held from Friday, October 31, to Tuesday, December 2, 1828.  It featured a re-match between incumbent President John Quincy Adams, and Andrew Jackson, who won a plurality of the electoral college vote in the 1824 election.  With no other major candidates, Jackson and his chief ally Martin Van Buren consolidated their bases in the South and New York and easily defeated Adams.  The Democratic Party merged its strength from the existing supporters of Jackson and their coalition with some of the supporters of William H. Crawford (the "Old Republicans") and Vice-President John C. Calhoun.  Jackson was the first president whose home state was neither Massachusetts nor Virginia.

Policy: A policy is a deliberate system of principles to guide decisions and achieve rational outcomes.  A policy is a statement of intent, and is implemented as a procedure or protocol.  Policies are generally adopted by a governance body within an organization.  Policies can assist in both "subjective" and "objective" decision making.  Policies to assist in subjective decision making usually assist senior management with decisions that must be based on the relative merits of a number of factors, and as a result are often hard to test objectively, e.g. work-life balance policy.  In contrast policies to assist in objective decision making are usually operational in nature and can be objectively tested, e.g. password policy.

The Heritage Foundation: The Heritage Foundation (abbreviated to Heritage) is an American conservative think tank based in Washington, D.C. The foundation took a leading role in the conservative movement during the presidency of Ronald Reagan, whose policies were taken from Heritage's policy study "Mandate for Leadership".  Heritage has since continued to have a significant influence in U.S. public policy making, and is considered to be one of the most influential conservative research organizations in the United States.  After the 2016 election of Donald Trump as U.S. President, Heritage leader Rebekah Mercer played a major role in shaping his transition team.

Heritage Canada: Heritage Canada The National Trust (formerly known as the Heritage Canada Foundation) (French: "Héritage Canada La Fiducie nationale" ), is a registered charity with the mandate to inspire and lead action to save historic places, and promote the care and wise use of our historic environment.  Its sites, projects and programs enhance community and quality of life and inspire Canadians to identify, conserve, use, celebrate and value their heritage buildings, landscapes, natural areas and communities for present and future generations.  Established in 1973, it has campaigned to update and fill gaps in Canadian heritage policies and laws, including supporting legislation such as Heritage Lighthouse Protection Act.  Heritage Canada also awards municipalities for their actions in preserving historical built environments through the Prince of Wales Prize for Municipal Heritage Leadership.

Question: What number was the president whose policies were taken from Heritage's policy study "Mandate for Leadership"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "president_name": {
      "type": "string",
      "description": "The name of the president whose policies were influenced by the specified study."
    },
    "presidential_number": {
      "type": "integer",
      "description": "The ordinal number of the president."
    },
    "policy_source_study": {
      "type": "string",
      "description": "The name of the policy study that influenced the president's policies."
    },
    "influencing_organization": {
      "type": "string",
      "description": "The organization that produced the influencing policy study."
    }
  },
  "required": [
    "president_name",
    "presidential_number",
    "policy_source_study",
    "influencing_organization"
  ],
  "additionalProperties": false
}
