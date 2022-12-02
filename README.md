# CyberwarfareTopicPresentation

For Global team
- Topic: Advanced War zones  (tentative) (55-60 min)

  - Introduction (15 min)
    - Why Virtual war?
    - Virtual War strategy with an example
    - Threats
    
  - Timeline of various attacks executed in War (20 min)
    - Major Malware involved
    - Risk and Losses
    
  - Detective measures (10 min)
    - Recomendations to nave users
  - Q&A (10 min)



For our team

- Topic: Malware involvement in Russia Ukrain War (tentative) (45 min)

  - Introduction (10 min)
    - Why Virtual war?
    - Virtual War strategy with an example
     
  - Timeline of various attacks executed in War (30 min)
    - Major Malware involved
    - Various hacking tools involved
    - kill chain of attacks
    - Recomendations to Analysts/Security engineers
    - Various yara rules for the malware discussed.
  - Q&A (5 min)


- Major Malware
  - FoxBlade (HermeticWiper), 
  - Lasainraw (IsaacWiper) DesertBlade, 
  - FiberLake, 
  - SonicVote CaddyWiper 
  - Industroyer2.
  
  
  
  IOCS
 - HermeticRansom AKA PartyTicket 
    •	4dc13bb83a16d4ff9865a51b3e4d24112327c526c1392e14d56f20d6f4eaf382 
    HermeticWizard and IsaacWiper  
    •	6983f7001de10f4d19fc2d794c3eb534 
    •	bdf30adb4e19aff249e7da26b7f33ead 
    •	d57f1811d8258d8d277cd9f53657eef9 
    •	0e84aff18d42fc691cb1104018f44403c325ad21 
    •	23873bf2670cf64c2440058130548d4e4da412dd 
    •	379ff9236f0f72963920232f4a0782911a6bd7f7 
    •	3c54c9a49a8ddca02189fe15fea52fe24f41a86f 
    •	61b25d11392172e587d8da3045812a66c3385451 
    •	6b5958bfabfe7c731193adb96880b225c8505b73 
    •	736a4cfad1ed83a6a0b75b0474d5e01a3a36f950 
    •	87bd9404a68035f8d70804a5159a37d1eb0a3568 
    •	912342f1c840a42f6b74132f8a7c4ffe7d40fb77 
    •	ac5b6f16fc5115f0e2327a589246ba00b41439c2 
    •	ad602039c6f0237d4a997d5640e92ce5e2b3bba3 
    •	b33dd3ee12f9e6c150c964ea21147bf6b7f7afa9 
    •	e9b96e9b86fad28d950ca428879168e0894d854f 
    •	f32d791ec9e6385a91b45942c230f52aff1626df 
    •	23ef301ddba39bb00f0819d2061c9c14d17dc30f780a945920a51bc3ba0198a4 
    •	2c7732da3dcfc82f60f063f2ec9fa09f9d38d5cfbe80c850ded44de43bdb666d 
    •	3c2fe308c0a563e06263bbacf793bbe9b2259d795fcc36b953793a7e499e7f71 
- HermeticWiper 
    •	912342F1C840A42F6B74132F8A7C4FFE7D40FB77 
    •	61B25D11392172E587D8DA3045812A66C3385451 
    
 - RECOMMENDATIONS
  - HermeticWizard:  
            •	Monitor traffic on the ports HermeticWizard uses to worm through networks. 

            HermeticRansom (aka PartyTicket) has decryption instructions: 
            •	According to researchers at CrowdStrike, HermeticRansom’s AES key used for encryption is recoverable. The Go script provided by CrowdStrike decrypts files encrypted by HermeticRansom.  
            •	
            o	The script takes the file to be decrypted as an argument via the “-p” flag and saves the decrypted output to “decrypted.bin” in the same directory. The script can be built as an executable or run via the Go run package.  


            CISA’s recommendations apply for HermeticWiper (aka DriveSlayer), HermeticRansom, and IsaacWiper: 
           - Regularly Review Your Cyber Hygiene 
            
            o	Validate that all remote access to the organization’s network and privileged or administrative access requires multi-factor authentication. 
            o	Ensure that software is up to date, prioritizing updates that address known exploited vulnerabilities identified by CISA. 
            o	Confirm that the organization’s IT personnel have disabled all ports and protocols that are not essential for business purposes. 
            o	If the organization is using cloud services, ensure that IT personnel have reviewed and implemented strong controls outlined in CISA's guidance. 
           - Quickly Detect a Potential Intrusion 
            •	
            o	Ensure that cybersecurity/IT personnel are focused on identifying and quickly assessing any unexpected or unusual network behavior. 
            o	Enable logging in order to better investigate issues or events. 
            o	Confirm that the organization's entire network is protected by antivirus/antimalware software and that signatures in these tools are updated. 
            o	If working with Ukrainian organizations, take extra care to monitor, inspect, and isolate traffic from those organizations; closely review access controls for that traffic. 
        - Prepare to Respond if an Intrusion Occurs 
            •	
            o	Designate a crisis-response team with main points of contact for a suspected cybersecurity incident and roles/ responsibilities within the organization, including technology, communications, legal, and business continuity. 
            o	Assure availability of key personnel; identify means to provide surge support for responding to an incident. 
            o	Conduct a tabletop exercise to ensure that all participants understand their roles during an incident. 
           - Maximize Your Organization’s Resilience to a Destructive Cyber Incident 
            •	
            o	Test backup procedures to ensure that critical data can be rapidly restored if the organization is impacted by ransomware or a destructive cyberattack; ensure that backups are isolated from network connections. 
            •	
            o	If using industrial control systems or operational technology, conduct a test of manual controls to ensure that critical functions remain operable if the organization’s network is unavailable or untrusted. 


