/*
Owner: Swapnl Dubey
Description: APB AGENT CONFIG
*/

`ifndef CFS_APB_AGENT_CONFIG_SV
	`define CFS_APB_AGENT_CONFIG_SV
	
class apb_agent_config extend uvm_component;

 funtion new(string name = "", uvm_component parent);
 super.new(name,parent);
 endfunction
 
 //virtual interface-------------------------
 local cfs_apb_vif vif;

//--------getter and setter for the apb interface----------

//setter-------------------
virtual function void set_vif(cfs_apb_vif value);
if(vif = null) begin
vif = value;
end
else begin
`uvm_fatal("ALGORITHM ISSUE: MUTIPLE ATTEMPT FOR APB AGENT SET");
 end
 endfuntion

//getter-------------------
virtual function get_vif();
return vif;
endfunction

/////////////////////////////////////////////////////////////////////////
virtual function void start_of_simulation_phase(uvm_phase phase);
super.start_of_simulation_phase(phase);
if(get_vif() == null) begin
`uvm_fatal("ALGORITHM ISSUE")
end
else begin
`uvm_fatal("APB_CONFIG",UVM_DEBUG)
end
endfunction
endclass
`endif
