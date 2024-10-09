## A simple customizable python script which you can use to get commands to use during CTFs. 

The script relies on a customizable YAML file which you can edit with your own commands you'd like to reuse.  

### Edit the `cmd_config.yml` file as follows:
* Put each phase such as `initial_enum` under the root 'category' heading
* Under each category, group the commands by tool
* Under each tool provide the different types of commands you can run, e.g. standard nmap scan, or all ports scan etc.
* Use `<IP>` and `<DOMAIN>` as placeholders for the ip and domain values passed to the script

### Install the requirements:
``` bash
pip install -r requirements.txt
```

### Run the script with:
``` bash
python3 main.py -i <IP> -d <DOMAIN> #Domain is optional
```

### Example:
<pre>
<span style="background-color:#06989A"><font color="#333333">Description: </font></span>
<span style="background-color:#06989A"><font color="#333333">Run nmap scan against all TCP ports</font></span>

<font color="#48B9C7">sudo nmap -sC -sV -T4 -A -p- </font><font color="#4E9A06">192.168.0.1</font>

<font color="#CC0000"><b>&gt; </b></font><span style="background-color:#06989A"><b>STANDARD</b></span>                                                                                                                                                                                    
  ALL TCP                                                                                                                                                                                     
  ALL UDP                                                                                                                                                                                     
  VULN                                                                                                                                                                                        
  GO BACK                                                                                                                                                                                     
</pre>

### Contributing
Feel free to raise a PR with your suggestions or additinal commands to add to the YAML file
