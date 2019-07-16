while read -r line
do
	export RunNumber=$(echo $line | awk -F',' '{printf "%u", $1}' | tr -d '"')
	# 20 variables so use field 1->20
	export field1=$(echo $line | awk -F',' '{printf "%s", $2}' | tr -d '"')
	export field2=$(echo $line | awk -F',' '{printf "%s", $3}' | tr -d '"')
	export field3=$(echo $line | awk -F',' '{printf "%s", $4}' | tr -d '"')
	export field4=$(echo $line | awk -F',' '{printf "%s", $5}' | tr -d '"')
	export field5=$(echo $line | awk -F',' '{printf "%s", $6}' | tr -d '"')
	export field6=$(echo $line | awk -F',' '{printf "%s", $7}' | tr -d '"')
	export field7=$(echo $line | awk -F',' '{printf "%s", $8}' | tr -d '"')
	export field8=$(echo $line | awk -F',' '{printf "%s", $9}' | tr -d '"')
	export field9=$(echo $line | awk -F',' '{printf "%s", $10}' | tr -d '"')
	export field10=$(echo $line | awk -F',' '{printf "%s", $11}' | tr -d '"')
	export field11=$(echo $line | awk -F',' '{printf "%s", $12}' | tr -d '"')
	export field12=$(echo $line | awk -F',' '{printf "%s", $13}' | tr -d '"')
	export field13=$(echo $line | awk -F',' '{printf "%s", $14}' | tr -d '"')
	export field14=$(echo $line | awk -F',' '{printf "%s", $15}' | tr -d '"')
	export field15=$(echo $line | awk -F',' '{printf "%s", $16}' | tr -d '"')
	export field16=$(echo $line | awk -F',' '{printf "%s", $17}' | tr -d '"')
	export field17=$(echo $line | awk -F',' '{printf "%s", $18}' | tr -d '"')
	export field18=$(echo $line | awk -F',' '{printf "%s", $19}' | tr -d '"')
	export field19=$(echo $line | awk -F',' '{printf "%s", $20}' | tr -d '"')
	export field20=$(echo $line | awk -F',' '{printf "%s", $21}' | tr -d '"')

	echo "runNumber $RunNumber"

	# run vensim with the template populated with field values
	eval "envsubst < batch-process-template.cmd > run-${RunNumber}.cmd"
	
	# evoke vensim
	eval "/cygdrive/c/Program\ Files\ \(x86\)/VensimDSS/vensim 'E:\fish-energy-tradeoff-vensim\run-$RunNumber.cmd'"

	eval "mv /cygdrive/e/fish-energy-tradeoff-vensim/run-$RunNumber.cmd /cygdrive/e/fish-energy-tradeoff-vensim/batch_process_commands/run-$RunNumber.cmd"

	eval "rm /cygdrive/e/fish-energy-tradeoff-vensim/fish-energy-run-$RunNumber.vdf"
done < MissingRunRecords3.csv




