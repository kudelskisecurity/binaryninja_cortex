from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="SAM3U"
    ROM_OFF=0x00080000 
    RAM_OFF=0x20000000 
    NFCRAM_OFF=0x20100000
    IRQ=MCU.IRQ+ [
        "NVIC_SUPC_IRQ",
        "NVIC_RSTC_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_RTT_IRQ",
        "NVIC_WDT_IRQ",
        "NVIC_PMC_IRQ",
        "NVIC_EEFC0_IRQ",
        "NVIC_EEFC1_IRQ",
        "NVIC_UART_IRQ",
        "NVIC_SMC_IRQ",
        "NVIC_PIOA_IRQ",
        "NVIC_PIOB_IRQ",
        "NVIC_PIOC_IRQ",
        "NVIC_USART0_IRQ",
        "NVIC_USART1_IRQ",
        "NVIC_USART2_IRQ",
        "NVIC_USART3_IRQ",
        "NVIC_HSMCI_IRQ",
        "NVIC_TWI0_IRQ",
        "NVIC_TWI1_IRQ",
        "NVIC_SPI_IRQ",
        "NVIC_SSC_IRQ",
        "NVIC_TC0_IRQ",
        "NVIC_TC1_IRQ",
        "NVIC_TC2_IRQ",
        "NVIC_PWM_IRQ",
        "NVIC_ADC12B_IRQ",
        "NVIC_ADC_IRQ",
        "NVIC_DMAC_IRQ",
        "NVIC_UDPHS_IRQ",
        ]
