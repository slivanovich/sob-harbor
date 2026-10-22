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
Sri Lankan honours system: The Sri Lankan national honours system is a fully indigenous honours system of titles, decorations and medals which are awarded to recognize achievements of, or service by, Sri Lankans or others in connection with Sri Lanka.  Until 1972, the British honours system was in place in Ceylon along with several indigenous titles (which were not awarded since 1948), however since 1956 no nominations were made for these honors and were automatically discontinued after Sri Lanka became a republic.  Since 1981 a uniquely Sri Lankan system of National Honours have been introduced.  These awards are titles that can be used by the recipients.

List of Victoria Cross recipients (N–Z): The Victoria Cross (VC) is the highest award of the United Kingdom honours system.  It is awarded for gallantry "in the face of the enemy" to members of the British armed forces.  It may be awarded posthumously.  It was previously awarded to Commonwealth countries, most of which have established their own honours systems and no longer recommend British honours.  It may be awarded to a person of any military rank in any service and to civilians under military command although no civilian has received the award since 1879.  Since the first awards were presented by Queen Victoria in 1857, two thirds of all awards have been personally presented by the British monarch.  These investitures are usually held at Buckingham Palace.

Victoria Cross: The Victoria Cross (VC) is the highest award of the United Kingdom honours system.  It is awarded for gallantry "in the face of the enemy" to members of the British armed forces.  It may be awarded posthumously.  It was previously awarded to Commonwealth countries, most of which have established their own honours systems and no longer recommend British honours.  It may be awarded to a person of any military rank in any service and to civilians under military command although no civilian has received the award since 1879.  Since the first awards were presented by Queen Victoria in 1857, two thirds of all awards have been personally presented by the British monarch.  These investitures are usually held at Buckingham Palace.

Victoria Cross (Canada): The Victoria Cross (VC) is the highest award of the United Kingdom honours system.  It was previously awarded to Canada and other Commonwealth countries, most of which including Canada have established their own honours systems and no longer recommend British honours.  Today, the Victoria Cross (French: "Croix de Victoria" ), created in 1993 and named in honour of the British Victoria Cross is the highest award within the Canadian honours system, taking precedence over all other orders, decorations, and medals.  It is awarded by either the Canadian monarch or his or her viceregal representative, the Governor General of Canada, to any member of the Canadian Forces or allies serving under or with Canadian military command for extraordinary valour and devotion to duty while facing hostile forces.  Whereas in many other Commonwealth countries the relevant version of the Victoria Cross can only be awarded for actions against the enemy in a wartime setting, the Canadian government has a broader definition of the term "enemy", and so the Victoria Cross can be awarded for action against armed mutineers, pirates, or other such hostile forces without war being officially declared.  Recipients are entitled to use the post-nominal letters "VC" (for both English and French) and also to receive an annuity of C$3,000.  The decoration has not been awarded since its inception.

Leslie Manser: Leslie Thomas Manser VC (11 May 1922 – 31 May 1942) was a British bomber pilot and recipient of the Victoria Cross, which was awarded posthumously following an attack on the German city of Cologne.

Imtiazi Sanad: Imtiazi Sanad is the fifth-highest Pakistani military award for gallantry or distinguished service in combat.  It can be conferred upon any member of the Pakistani Armed Forces or paramilitary forces who is mentioned in the dispatches of a senior commander for actions that do not warrant a gallantry award.  It may be considered equivalent of the Mentioned in Despatches in the Commonwealth honours system and the Bronze Star in the United States honours system.  The next highest award in the Pakistani honours systems is the Tamgha-i-Jurat.

Medal of Honour (Hong Kong): The Medal of Honour (Chinese: 榮譽勳章, MH) is part of the honours system in Hong Kong.  It was created in 1997 to replace the British honours system after the transfer of sovereignty to the People's Republic of China and the establishment of Hong Kong Special Administrative Region.  The Medal of Honour, is the entry level award under the Hong Kong honours system and is awarded for community service in a district or in a particular area for a long period of time.  It may also be awarded to civil servants for serving with distinction.

Orders, decorations, and medals of Zimbabwe: The Zimbabwean honours system was instituted in late 1980 to replace the Rhodesian honours system.  The first award that was instituted was the Independence Medal, which was awarded to those who were involved in the Zimbabwean independence commemorations in some way.  The Zimbabwean honours system includes a range of orders, gallantry decorations, gallantry medals, and service medals.

Papua New Guinea honours system: The Papua New Guinea honours system is the main system of honouring citizens of Papua New Guinea for their services to the country, it consists of three Orders and several medals.  After independence, Papua New Guinea used the Imperial honours system, however, in recognition of the nation's 30th anniversary, a new awards system was adopted.  The official announcement of its creation was made by Prime Minister Sir Michael Somare on 12 November 2004 and the first investitures were performed by the Princess Royal in early October 2005.  The old honours system is still in use as well, however, and the Queen issues a Papua New Guinean List as part of every Birthday and New Year Honours List.

List of Australian Victoria Cross recipients: The Victoria Cross (VC) is a military decoration awarded for valour "in the presence of the enemy" to members of the Australia Armed Forces.  It may be awarded to a person of any in any service, and to civilians under military command.  Being the highest award in the Australian Honours Order of Wearing, the Victoria Cross takes precedence over all other postnominals and Australian orders and decorations.  The Victoria Cross was instituted by Queen Victoria in 1856, initially to reward acts of valour during the Crimean War.  Because of its rarity and inherent significance, the VC is highly prized, both as an award and as a collector's item, with one medal being sold for over A$1 million at auction.  Australians have received the Victoria Cross under the Imperial honours system and later under the Australian Honours System, when in 1991 a new but equivalent award was established by letters patent within the Commonwealth of Australia and its Territories, known as the Victoria Cross for Australia.  The Victoria Cross for Australia has been awarded four times: twice to Special Air Service Regiment members, once to a member of the 6th Battalion, Royal Australian Regiment, and a posthumous award to a member of the 2nd Commando Regiment.  All four were for actions in the War in Afghanistan.

Question: The award which Leslie Manser collected was the  highest award of which  honours system

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_name": {
      "type": "string",
      "description": "The name of the award received."
    },
    "honours_system": {
      "type": "string",
      "description": "The name of the honours system to which the award belongs."
    },
    "award_status_in_system": {
      "type": "string",
      "description": "The status or rank of the award within its honours system (e.g., highest award)."
    },
    "recipient_name": {
      "type": "string",
      "description": "The name of the person who received the award."
    }
  },
  "required": [
    "award_name",
    "honours_system",
    "award_status_in_system",
    "recipient_name"
  ],
  "additionalProperties": false
}
