<script lang="ts">
	import { WEBUI_NAME } from '$lib/stores';
</script>

<div class="flex flex-col h-full justify-between space-y-3 text-sm mb-6">
	<div class=" space-y-3 overflow-y-scroll max-h-[28rem] lg:max-h-full">
		<div>
			<div class=" mb-2.5 text-sm font-medium flex space-x-2 items-center">
				<div>{$WEBUI_NAME}</div>
			</div>
			<div class="flex w-full justify-between items-center">
				<div class="flex flex-col text-xs text-gray-700 dark:text-gray-200">
					<div class="flex gap-1">Try harder :))</div>
				</div>
			</div>
		</div>

		<hr class=" border-gray-100 dark:border-gray-850" />

		<div class="flex space-x-1">
			<a href="https://discord.gg/5rJgQTnV4s" target="_blank">
				<img
					alt="Discord"
					src="https://img.shields.io/badge/Discord-Open_WebUI-blue?logo=discord&logoColor=white"
				/>
			</a>

			<a href="https://twitter.com/OpenWebUI" target="_blank">
				<img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/OpenWebUI" />
			</a>

			<a href="https://github.com/open-webui/open-webui" target="_blank">
				<img
					alt="Github Repo"
					src="https://img.shields.io/github/stars/open-webui/open-webui?style=social&label=Star us on Github"
				/>
			</a>
		</div>
	</div>
</div>
