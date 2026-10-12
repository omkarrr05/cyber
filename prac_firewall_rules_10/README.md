# Practical 10 - Firewall Configuration and Rule-based Filtering

This practical contains **no program code**. It is done in Windows Defender Firewall
with Advanced Security (GUI). The only command used is `nslookup`.

## A. Port rule
- Inbound Rules -> New Rule -> Port -> TCP, specific local ports `80,443`
  -> Block the connection -> all profiles -> name `http_block`.
- Outbound Rules -> New Rule -> Port -> TCP, ports `80,443`
  -> Block the connection -> name `http_block outbound rule`.

## B. Custom rule (block by IP)
- In CMD run:  `nslookup www.amazon.com`
- Inbound Rule -> Custom -> All programs -> Scope: add Amazon's IP addresses
  -> Block -> name `https_blocksin`.
- Outbound Rule -> Custom -> same scope -> Block -> name `https_blocksout`.

## C. Program rule
- New Rule -> Program -> select the .exe to block -> Block the connection
  -> name `EXE_BLOCKOUT` (create for Outbound, verify the program is blocked).
